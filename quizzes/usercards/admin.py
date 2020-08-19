from django.contrib import admin
from .models import User, UserCard, QuizzesProgress

admin.site.register(User)
admin.site.register(UserCard)
admin.site.register(QuizzesProgress)