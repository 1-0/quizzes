from django.contrib import admin
from .models import Quizzes, Question, Answer, Comment

admin.site.register(Quizzes)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
