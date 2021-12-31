from django.urls import path
from .views import UserRegisterApi

urlpatterns = [
    path('', UserRegisterApi.as_view())
]
