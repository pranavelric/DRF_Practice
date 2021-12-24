import json

from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_view(request):
    if request.method == 'GET':
        print(request.method)
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

        # pythondata = json.loads(str(request.body,encoding='utf-8'))
        id = pythondata.get('id', None)


        if id is not None:
            stu = Student.objects.get(id=id)
            ser = StudentSerializer(stu)
            json_data = JSONRenderer().render(ser.data)
            return HttpResponse(json_data, content_type='application/json')


        stu = Student.objects.all()
        ser = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(ser.data)
        return HttpResponse(json_data, content_type='application/json')
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        ser = StudentSerializer(data=pythondata)
        if ser.is_valid():
            ser.save()
            msg = {'msg':'saved'}
            json_data = JSONRenderer().render(msg)
            return  HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(ser.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id= pythondata.get('id')
        stu = Student.objects.get(id=id)
        ser = StudentSerializer(stu,data=pythondata,partial=True)
        if ser.is_valid():
            ser.save()
            msg = {'msg': 'saved'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(ser.errors)
        return HttpResponse(json_data, content_type='application/json')
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        msg = {'msg':'deleted'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')





