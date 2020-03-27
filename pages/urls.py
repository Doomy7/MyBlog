
from django.urls import path

from . import views
#'pages' urls
urlpatterns = [
    path('', views.index, name='index'),
]