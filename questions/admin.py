from django.contrib import admin

from questions.models import Post, Answer, Like

# Register your models here.
admin.site.register(Post)
admin.site.register(Answer)
admin.site.register(Like)