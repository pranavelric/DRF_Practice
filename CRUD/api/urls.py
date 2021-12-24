from django.urls import path
from .views import student_view
from django.views.generic import RedirectView

urlpatterns = [
    path('api/', student_view),
    path('', RedirectView.as_view(url='/api/'))
]
