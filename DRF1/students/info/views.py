from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentsSerializer
from rest_framework.renderers import  JSONRenderer

def student_view(request):
    stu = Student.objects.all()
    ser = StudentsSerializer(stu,many=True)
    # json = JSONRenderer().render(ser.data)
    # return HttpResponse(json,content_type="application/json")
    return JsonResponse(ser.data,safe=False)


def single_student(request,pk):
    stu = Student.objects.get(id= pk)
    ser = StudentsSerializer(stu)
    return JsonResponse(ser.data)