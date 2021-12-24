from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import Student_serializer


@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):

    def get(self, request, *args, **kwargs):

        json_data = request.body

        stream = io.BytesIO(json_data)

        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)
            ser = Student_serializer(stu)
            json_data = JSONRenderer().render(ser.data)
            return HttpResponse(json_data, content_type='application/json')

            # return JsonResponse(ser.data, safe=False)
        stu = Student.objects.all()
        ser = Student_serializer(stu, many=True)
        json_data = JSONRenderer().render(ser.data)
        return HttpResponse(json_data, content_type='application/json')
        # return JsonResponse(ser.data, safe=False)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        ser = Student_serializer(data=pythondata)
        if ser.is_valid():
            ser.save()
            msg = {'msg': 'saved'}
            return JsonResponse(msg, safe=False)

        return JsonResponse(ser.errors, safe=False)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        ser = Student_serializer(stu, data=pythondata, partial=True)
        if ser.is_valid():
            ser.save()
            msg = {'msg': 'updated'}
            return JsonResponse(msg, safe=False)
        return JsonResponse(ser.errors, safe=False)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        msg = {'msg': 'deleted'}
        return JsonResponse(msg, safe=False)
