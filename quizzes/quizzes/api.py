from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Quizzes, Question, Answer, Comment, FS
from ninja import NinjaAPI
from ninja.security import django_auth

api1 = NinjaAPI()
# http://127.0.0.1:8000/api1/docs#/default


@api1.get("/get_quizzes", auth=django_auth)
def quizzes(request, quizzes_id: int = 0, user_id: int = 0):
    """quizzes(request, quizzes_id: int = 0, user_id: int = 0) - return quizzes"""
    res = {}
    res_quizzes = {}
    if user_id:
        # http://127.0.0.1:8000/api1/get_quizzes?user_id=1
        try:
            User.objects.get(pk=user_id)
        except User.DoesNotExist:
            res['Error'] = "No user id=%s" % (user_id,)
            return res
        quizzes_all = Quizzes.objects.filter(q_person_id=user_id)
        for q in quizzes_all:
            cur_q = {"title": q.title, "content": q.content}
            if q.photo:
                cur_q["photo"] = q.photo.name
            res_quizzes[q.id] = cur_q
        res['quizzes'] = res_quizzes
    elif quizzes_id:
        # http://127.0.0.1:8000/api1/get_quizzes?quizzes_id=6
        try:
            q = Quizzes.objects.get(pk=quizzes_id)
            cur_q = {"title": q.title, "content": q.content}
            if q.photo:
                cur_q["photo"] = q.photo.name
            res['quizzes'] = cur_q
        except Quizzes.DoesNotExist:
            res['Error'] = "No quizzes id=%s" % (quizzes_id, )
    else:
        # http://127.0.0.1:8000/api1/get_quizzes
        quizzes_all = Quizzes.objects.all()
        for q in quizzes_all:
            cur_q = {"title": q.title, "content": q.content}
            if q.photo:
                cur_q["photo"] = q.photo.name
            res_quizzes[q.id] = cur_q
        res['quizzes'] = res_quizzes
    return res


@login_required
@api1.get("/get_questions", auth=django_auth)
def questions(request, quizzes_id: int = 0, question_id: int = 0):
    """questions(request, quizzes_id: int = 0, question_id: int = 0) - return questions"""
    res = {}
    res_questions = {}
    if quizzes_id:
        # http://127.0.0.1:8000/api1/get_questions?quizzes_id=6
        questions_all = Question.objects.filter(quizzes=quizzes_id)
        for q in questions_all:
            cur_q = {"content": q.content}
            if q.photo:
                cur_q["photo"] = q.photo.name
            res_questions[q.id] = cur_q
        res['questions'] = res_questions
    elif question_id:
        # http://127.0.0.1:8000/api1/get_questions?question_id=1
        try:
            q = Question.objects.get(pk=question_id)
            cur_q = {"quizzes": q.quizzes.id, "content": q.content}
            if q.photo:
                cur_q["photo"] = q.photo.name
            res['question'] = cur_q
        except Question.DoesNotExist:
            res['Error'] = "No question id=%s" % (question_id, )
    else:
        res['Error'] = "No questions"
    return res


@login_required
@api1.get("/get_answers", auth=django_auth)
def answers(request, question_id: int = 0, answer_id: int = 0):
    """answers(request, question_id: int = 0, answer_id: int = 0) -
    return answers"""
    res = {}
    res_answers = {}
    if question_id:
        # http://127.0.0.1:8000/api1/get_answers?question_id=1
        answers_all = Answer.objects.filter(question=question_id)
        for a in answers_all:
            cur_a = {"content": a.content}
            if a.photo:
                cur_a["photo"] = a.photo.name
            res_answers[a.id] = cur_a
        res['answers'] = res_answers
    elif answer_id:
        try:
            a = Answer.objects.get(pk=answer_id)
            cur_a = {"question": a.question.id, "content": a.content}
            if a.photo:
                cur_a["photo"] = a.photo.name
            res['answer'] = cur_a
        except Answer.DoesNotExist:
            res['Error'] = "No answers id=%s" % (answer_id, )
    else:
        res['Error'] = "No answers"
    return res


@api1.get("/get_comments", auth=django_auth)
def comments(request, quizzes_id: int = 0, user_id: int = 0, comment_id: int = 0):
    """comments(request, quizzes_id: int = 0, user_id: int = 0, comment_id: int = 0) -
    return comments"""
    res = {}
    comments = {}
    if quizzes_id:
        # http://127.0.0.1:8000/api1/get_comments?quizzes_id=6
        comments_all = Comment.objects.filter(quizzes=quizzes_id)
        for c in comments_all:
            cur_c = {
                "person_id": c.person_id,
                "person_username": c.person.username,
                "content": c.content
            }
            comments[c.id] = cur_c
        res['comments'] = comments
    elif user_id:
        # http://127.0.0.1:8000/api1/get_comments?user_id=2
        comments_all = Comment.objects.filter(person_id=user_id)
        for c in comments_all:
            cur_c = {
                "quizzes_id": c.quizzes_id,
                "content": c.content
            }
            comments[c.id] = cur_c
        res['comments'] = comments
    elif comment_id:
        # http://127.0.0.1:8000/api1/get_comments?comment_id=1
        try:
            c = Comment.objects.get(pk=comment_id)
            cur_c = {
                "quizzes_id": c.quizzes_id,
                "person_id": c.person_id,
                "person_username": c.person.username,
                "content": c.content
            }
            comments[c.id] = cur_c
            res['comment'] = comments
        except Comment.DoesNotExist:
            res['Error'] = "No comments id=%s" % (comment_id,)
    else:
        res['Error'] = "No id's for get comments"
    return res
