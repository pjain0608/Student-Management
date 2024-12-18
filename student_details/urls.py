from django.urls import path
from . import views
from django.shortcuts import render, redirect

urlpatterns = [
    path('',views.index, name = 'main'),
    path('2',views.pyspiders, name = 'pyspiders'),
    path('3',views.qspiders, name = 'qspiders'),
    path('4',views.jspiders, name = 'jspiders'),
    path('5',views.prospiders, name = 'prospiders'),
    path('stud/<int:pk>',views.student, name = 'student'),
    path('std/<int:ab>',views.edit, name = 'edit'),
    path('create',views.create, name = 'create'),
]