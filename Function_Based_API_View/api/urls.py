from .views import hello_world
from django.views.generic import RedirectView
from django.urls import path

urlpatterns = [
    path('api/', hello_world),
    path('api/<int:pk>', hello_world),
    path('', RedirectView.as_view(url='/api/'))
]
