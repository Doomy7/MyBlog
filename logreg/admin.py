from django.contrib import admin
from .models import users, articles, comments, likes
# Register your models here.

class UsersInline(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'dob', 'phone', 'interests','bio')

class ArticlesInline(admin.ModelAdmin):
    list_display = ( 'aid', 'article_author', 'title', 'details', 'category', 'likesNo', 'commentsNo')
    def article_author(self, articles):
        return articles.user.username

class CommentsInline(admin.ModelAdmin):
    list_display = ('article_title', 'comment_poster',  'comment')
    def article_title(self, comments):
        return comments.aid.title
    def comment_poster(self, comments):
        return comments.uid.username

class LikesInline(admin.ModelAdmin):
    list_display = ('article_title' ,'liker')
    def article_title(self, likes):
        return likes.aid.title
    def liker(self, likes):
        return likes.uid.username

admin.site.register(users, UsersInline)
admin.site.register(articles, ArticlesInline)
admin.site.register(comments, CommentsInline)
admin.site.register(likes, LikesInline)