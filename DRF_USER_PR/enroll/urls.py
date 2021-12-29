from django.urls import path
from .views import UserAddShowView


urlpatterns = [
    path('',UserAddShowView.as_view(),name="addandshow"),
]