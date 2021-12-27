from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongApi, SingerApi

router = DefaultRouter()
router.register('singer', SingerApi, basename='singer')
router.register('song', SongApi, basename='song')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
