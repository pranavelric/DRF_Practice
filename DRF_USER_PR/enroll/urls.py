from django.urls import path,include
from .views import UserAddShowView,DeleteUser,UserUpdateView


urlpatterns = [
    path('',UserAddShowView.as_view(),name="addandshow"),
    path('delete/<int:id>',DeleteUser.as_view(),name="deleteuser"),
    path('update/<int:id>',UserUpdateView.as_view(),name='updateuser'),
    path('api/',include('enroll.api.urls'))

]