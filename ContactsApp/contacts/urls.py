from django.urls import path
from .views import ContactList, ContactRUD

urlpatterns = [
    path('', ContactList.as_view()),
    path('<int:id>', ContactRUD.as_view())
]
