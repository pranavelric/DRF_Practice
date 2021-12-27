from django.urls import path,include
from .views import StudentApi
from django.views.generic import RedirectView

urlpatterns = [
    path('api/',StudentApi.as_view()),
    path('',RedirectView.as_view(url='api/')),
    path('auth/',include('rest_framework.urls'))

]