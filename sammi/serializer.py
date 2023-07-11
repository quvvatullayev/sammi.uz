from rest_framework import serializers
from .models import (
    AboutImg,
    News,
    NewsImg,
    Video,
    Gallery,
    GalleryImg,
    VideoGallery,
    Ad,
    MainStatistic,
    Quiz,
    UsefulSites,
    Contact,
)

class AboutImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImg
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class NewsImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImg
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class GalleryImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImg
        fields = '__all__'

class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = '__all__'

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

class MainStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainStatistic
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class UsefulSitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulSites
        fields = '__all__'


