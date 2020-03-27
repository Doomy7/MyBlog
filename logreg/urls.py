from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
#'logij' urls
app_name='logreg'
urlpatterns = [
    path('register/', views.regindex, name='regindex'),
    path('login/', views.logindex, name='logindex'),
    path('logout/', views.oust, name='oust'),
    path('profile/', views.profile, name='profile'),
    path('', views.kick, name='kick'),
    path('regart/', views.regart, name='regart'),
    path('seeart/<int:aid>', views.seeart, name='seeart'),
    path('seeart/comment/<int:aid>/<int:uid>', views.compost, name='compost'),
    path('seeart/like/<int:aid>/<int:uid>', views.like, name='like'),
    path('seeart/dislike/<int:aid>/<int:uid>', views.dislike, name='dislike'),
    path('feed/', views.feed, name='feed'),
    path('profile/delete/', views.delete, name='delete'),
    path('profile/delete/goodbye', views.delete_account, name='delete_account')
]