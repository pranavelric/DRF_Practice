from rest_framework import viewsets
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .serializers import StudentSerializer
from .models import Student


class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
