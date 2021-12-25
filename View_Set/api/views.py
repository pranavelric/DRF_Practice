from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student


class StudentApi(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        ser = StudentSerializer(stu, many=True)
        return Response(ser.data)

    def retrive(self,request,pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            ser = StudentSerializer(stu)
            return Response(ser.data)

    def create(self,request):
        ser = StudentSerializer(data= request.data)
        if ser.is_valid():
            ser.save()
            return  Response({'msg':'data saved'},status=status.HTTP_201_CREATED)
        return  Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id = pk
        stu =  Student.objects.get(id=id)
        ser = StudentSerializer(stu,data= request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg': 'data saved'}, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        stu = Student.objects.get(id=id)
        ser = StudentSerializer(stu, data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'msg': 'data saved'}, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        id = pk
        stu = Student.object.get(id=id)
        stu.delete()
        return  Response({'msg':'data deleted'})
