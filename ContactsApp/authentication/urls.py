from django.urls import path
from .views import UserRegisterApi,UserLoginApi

urlpatterns = [
    path('register', UserRegisterApi.as_view()),
    path('login',UserLoginApi.as_view())
]
