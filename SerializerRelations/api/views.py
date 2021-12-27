from .serializers import SingerSerializer, SongSerializer
from .models import Songs, Singer
from rest_framework import viewsets


class SingerApi(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongApi(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
