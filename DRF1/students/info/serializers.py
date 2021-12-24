from rest_framework import serializers


class StudentsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    standard = serializers.CharField(max_length=150)
    bio = serializers.CharField()
    roll = serializers.IntegerField()
