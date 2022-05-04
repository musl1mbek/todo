from .views import *
from django.urls import path

urlpatterns = [
    path("",HomePage,name='home'),
    path("change/<pk>",ChangePage,name='change'),
    path("delete/<pk>",DeletePage,name='delete'),
    path("path",PathPage,name='path'),
    path("completed",CompletedPage,name='completed'),
    path("active",ActivePage,name='active'),
    path("change-task",ChangeTaskPage,name='change-task'),
]


