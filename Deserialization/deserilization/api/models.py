from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=150)
    roll = models.IntegerField()
    city = models.CharField(max_length=150)

    def __str__(self):
        return self.name
