from django.urls import path
from tabla1 import views

urlpatterns = [
    path('', views.index),
]