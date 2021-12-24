from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name shoud start with R')

    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = ['id', 'name', 'city', 'roll']

    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('Seats fuull')
        return  value

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower()=='elric' and ct.lower()!='la':
            raise serializers.ValidationError('City must be la')
        return data


