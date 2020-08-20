from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Quizzes, Question, Answer, FS
from ninja import NinjaAPI

api1 = NinjaAPI()
# http://127.0.0.1:8000/api1/docs#/default


@login_required
@api1.get("/get_quizzes")
def quizzes(request, quizzes_id: int = 0, user_id: int = 0):
    res = {}
    quizzes = {}
    if not quizzes_id and not user_id:
        # http://127.0.0.1:8000/api1/get_quizzes
        quizzes_all = Quizzes.objects.all()
        for q in quizzes_all:
            cur_q = {"title": q.title, "content": q.content}
            if q.photo:
                cur_q["photo"] = q.photo.name
            quizzes[q.id] = cur_q
        res['quizzes'] = quizzes
    elif quizzes_id:
        # http://127.0.0.1:8000/api1/get_quizzes?quizzes_id=6
        try:
            q = Quizzes.objects.get(pk=quizzes_id)
            cur_q = {"title": q.title, "content": q.content}
            if q.photo:
                cur_q["photo"] = q.photo.name
            res['quizzes'] = cur_q
        except:
            res['Error'] = "No quizzes id=%s" % (quizzes_id, )
    elif user_id:
        # http://127.0.0.1:8000/api1/get_quizzes?user_id=1
        try:
            u = User.objects.get(pk=user_id)
        except:
            res['Error'] = "No user id=%s" % (user_id,)
            return res
        try:
            quizzes_all = Quizzes.objects.filter(q_person_id=user_id)
            for q in quizzes_all:
                cur_q = {"title": q.title, "content": q.content}
                if q.photo:
                    cur_q["photo"] = q.photo.name
                quizzes[q.id] = cur_q
            res['quizzes'] = quizzes
        except:
            res['Error'] = "No for user id=%s" % (user_id,)
    return res


@login_required
@api1.get("/get_questions")
def questions(request, quizzes_id: int = 0):
    res = {}
    questions = {}
    if quizzes_id:
        # http://127.0.0.1:8000/api1/get_questions?quizzes_id=6
        try:
            questions_all = Question.objects.filter(quizzes_id=quizzes_id)
            for q in questions_all:
                cur_q = {"content": q.content}
                if q.photo:
                    cur_q["photo"] = q.photo.name
                questions[q.id] = cur_q
            res['questions'] = questions
        except:
            res['Error'] = "No questions for quizzes id=%s" % (quizzes_id,)
    else:
        res['Error'] = "No quizzes id for get questions"
    return res


@login_required
@api1.get("/get_answers")
def answers(request, question_id: int = 0):
    res = {}
    answers = {}
    if question_id:
        # http://127.0.0.1:8000/api1/get_answers?question_id=6
        try:
            answers_all = Answer.objects.filter(question_id=question_id)
            for a in answers_all:
                cur_a = {"content": a.content}
                if a.photo:
                    cur_a["photo"] = a.photo.name
                answers[a.id] = cur_a
            res['answers'] = answers
        except:
            res['Error'] = "No answers for questions id=%s" % (question_id,)
    else:
        res['Error'] = "No questions id for get answers"
    return res
