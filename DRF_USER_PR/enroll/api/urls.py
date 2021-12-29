from rest_framework.routers import DefaultRouter
from .views import UserApi
from django.urls import path, include

router = DefaultRouter()
router.register('crud', UserApi, basename='user')

urlpatterns = [
    path('', include(router.urls)),

]
