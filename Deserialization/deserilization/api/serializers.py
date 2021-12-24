from rest_framework import serializers
from .models import Students


class ApiSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return Students.objects.create(**validated_data)
