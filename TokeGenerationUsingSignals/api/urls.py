from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import StudentApi

router = DefaultRouter()
router.register('api',StudentApi,basename='student')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]
