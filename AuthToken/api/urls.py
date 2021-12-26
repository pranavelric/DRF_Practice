from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentApi
from rest_framework.authtoken import views
from .customtoken import CustomAuthToken

router = DefaultRouter()

router.register('api', StudentApi, basename='studentapi')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('gettoken/',views.obtain_auth_token)
    path('gettoken/', CustomAuthToken.as_view())
]
