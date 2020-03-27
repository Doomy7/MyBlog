from django.contrib import admin
from .models import users, articles, comments, likes
# Register your models here.

admin.site.register(users)
admin.site.register(articles)
admin.site.register(comments)
admin.site.register(likes)