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

