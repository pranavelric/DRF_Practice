from django.urls import path,include
from django.views.generic import RedirectView
from .views import StudentList, StudentRUD


urlpatterns = [
    path('api/',StudentList.as_view()),
    path('api/<int:pk>',StudentRUD.as_view()),
    path('',RedirectView.as_view(url='/api/'))
]
