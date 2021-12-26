from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentApi

router = DefaultRouter()
router.register('studentapi', StudentApi, basename='student')

urlpatterns = [
    path('', include(router.urls))
]
