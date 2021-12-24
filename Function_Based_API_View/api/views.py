from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET', 'POST', 'PUT','PATCH','DELETE'])
def hello_world(request,pk=None):
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            ser = StudentSerializer(stu)
            return  Response(ser.data)
        stu = Student.objects.all()
        ser = StudentSerializer(stu,many=True)
        return  Response(ser.data)
    if request.method == 'POST':
        ser = StudentSerializer(data= request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'Data Saved!!!'})
        return  Response(ser.errors)
    if request.method=='PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        ser = StudentSerializer(stu,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg': 'Data Updated!!!'})
        return Response(ser.errors)
    if request.method=='PACTH':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        ser = StudentSerializer(stu,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'msg': 'Data Updated!!!'})
        return Response(ser.errors)
    if request.method=='DELETE':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return  Response({'msg':'DELETEED!!'})
