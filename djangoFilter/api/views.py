from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend


class StudentApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city','name']

