from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('../logout', views.logoutUser, name="logout")
]