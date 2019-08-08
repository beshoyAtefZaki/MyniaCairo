from django.urls import path
from .views import home,user_register



urlpatterns = [
    path('' , home ,name="home"),
    path('create/' ,user_register),
]
