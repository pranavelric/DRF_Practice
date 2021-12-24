from django.http import HttpResponse
from .models import Students
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import ApiSerializer
import io
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def students_view(request):
    o = Students.objects.all()
    print(o)
    print(request.method)

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        ser = ApiSerializer(data=python_data)

        if ser.is_valid():
            ser.save()
            msg = {'msg': 'saved'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(ser.errors)
        return HttpResponse(json_data, content_type='application/data')
    msg = {'msg': 'sdfasdfaved'}
    json_data = JSONRenderer().render(msg)
    return HttpResponse(json_data, content_type='application/json')

