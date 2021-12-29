from .serializers import UserSerializer
from enroll.models import User
from rest_framework import viewsets
from rest_framework.filters import  SearchFilter

class UserApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
