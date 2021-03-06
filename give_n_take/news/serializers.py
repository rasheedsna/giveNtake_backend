from rest_framework import serializers
from .models import *

class NewsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsType
        fields = ['id','name']
        

    def create(self,validated_data):
        news_type = NewsType.objects.create(**validated_data)
        return news_type
      

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id','title','description','meeting_link','news_type','news_image','date_added','date_expired','status']
        

    def create(self,validated_data):
        news = News.objects.create(**validated_data)
        return news

