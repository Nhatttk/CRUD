from django.urls import path
from . import views


urlpatterns = [
    path('student-list-bt', views.bootstrap, name='bootstrap'),
    path('student-list-tw', views.tailwind, name='tailwind'),
]