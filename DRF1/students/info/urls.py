from django.urls import path
from django.http import HttpResponse
from .views import student_view, single_student

urlpatterns = [
    path('students/',student_view),
    path('students/<pk>',single_student)
]