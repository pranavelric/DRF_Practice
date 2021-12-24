from django.urls import path

from django.views.generic import RedirectView
from .views import StudentApi
urlpatterns = [

    path('api/', StudentApi.as_view()),
    path('', RedirectView.as_view(url='/api/'))


]
