from rest_framework import serializers
from .models import Hashtag, SearchTask


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('name',)

    def exist(self, validated_data):
        tag = Hashtag.objects.filter(name=validated_data['name']).first()
        return tag.exists()
        
    def create(self, validated_data):
        tag = Hashtag.objects.filter(name=validated_data['name']).first()
        if tag is None:
            tag = Hashtag.objects.create(name=validated_data['name'])
        return tag


class SearchTaskSerializer(serializers.ModelSerializer):
    hashtag = HashtagSerializer()

    class Meta:
        model = SearchTask
        read_only_fields = ('updated_at', 'created_at')
        fields = ('task_id', 'hashtag', 'status')

    def create(self, validated_data):
        tag_data = validated_data['hashtag']
        tag = Hashtag.objects.filter(name=tag_data['name']).first()
        task = SearchTask.objects.create(hashtag=tag)
        return task