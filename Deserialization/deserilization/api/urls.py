from django.urls import path
from django.views.generic import RedirectView

from .views import students_view
urlpatterns = [
    path('api/',students_view),
    path('',RedirectView.as_view(url='/api/'))
]