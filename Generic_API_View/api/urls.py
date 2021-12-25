from django.urls import path
from django.views.generic import RedirectView
from .views import LCStudentApi,PUDStudentApi
urlpatterns = [
    path('api/',LCStudentApi.as_view()),
    path('api/<int:pk>',PUDStudentApi.as_view()),

    path('', RedirectView.as_view(url='/api/'))
]
