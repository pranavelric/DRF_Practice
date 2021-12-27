from rest_framework import serializers
from .models import Singer, Songs


class SingerSerializer(serializers.ModelSerializer):
    # songg = serializers.StringRelatedField(many=True)
    # songg = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    songg = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'songg']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['id', 'title', 'singer', 'duration']
