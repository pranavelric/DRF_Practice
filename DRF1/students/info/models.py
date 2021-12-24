from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=150)
    standard = models.CharField(max_length=150)
    bio = models.TextField()
    roll = models.IntegerField()

    def __str__(self):
        return self.name
