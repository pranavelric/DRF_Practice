from rest_framework import serializers
from enroll.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="userapi-detail")
    class Meta:
        model = User
        fields = ['id','name', 'email', 'password','url']

