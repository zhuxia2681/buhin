from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/list/', views.list_user, name='list_user'),
    path('staff/list/', views.list_staff, name='list_staff'),
]
