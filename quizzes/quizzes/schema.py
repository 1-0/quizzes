import graphene
from graphene_django import DjangoObjectType
from .models import Quizzes, Question, Answer, Comment


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "q_person", "content", "photo")
        # fields = ("id", "title", "q_person", "content", "photo", "published_datetime")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "quizzes", "photo", "content")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("id", "question", "photo", "content")


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ("id", "quizzes", "person", "content")
        # fields = ("id", "quizzes", "person", "published_datetime", "content")


class Query(graphene.ObjectType):
    all_quizzes = graphene.List(QuizzesType)
    quizzes_by_title = graphene.Field(QuizzesType, title=graphene.String(required=True))
    quizzes_by_id = graphene.Field(QuizzesType, id=graphene.Int(required=True))
    quizzes_by_person = graphene.List(QuizzesType, q_person=graphene.Int(required=True))
    questions_by_quizzes = graphene.List(QuestionType, quizzes=graphene.Int(required=True))
    answers_by_question = graphene.List(AnswerType, question=graphene.Int(required=True))
    comments_by_quizzes = graphene.List(CommentType, quizzes=graphene.Int(required=True))
    comments_by_person = graphene.List(CommentType, person=graphene.Int(required=True))

    def resolve_all_quizzes(root, info):
        return Quizzes.objects.all()

    def resolve_quizzes_by_title(root, info, title):
        try:
            return Quizzes.objects.get(title=title)
        except Quizzes.DoesNotExist:
            return None

    def resolve_quizzes_by_person(root, info, q_person):
        try:
            return Quizzes.objects.get(q_person=q_person)
        except Quizzes.DoesNotExist:
            return None

    def resolve_questions_by_quizzes(root, info, quizzes):
        try:
            return Question.objects.get(quizzes=quizzes)
        except Question.DoesNotExist:
            return None

    def resolve_answers_by_question(root, info, question):
        try:
            return Answer.objects.get(question=question)
        except Answer.DoesNotExist:
            return None

    def resolve_comments_by_quizzes(root, info, quizzes):
        try:
            return Comment.objects.get(quizzes=quizzes)
        except Comment.DoesNotExist:
            return None

    def resolve_comments_by_person(root, info, person):
        try:
            return Comment.objects.get(person=person)
        except Comment.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)









