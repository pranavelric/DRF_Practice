from rest_framework import serializers
from .models import Student


class Student_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    city = serializers.CharField(max_length=150)
    roll = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.save()
        return instance
