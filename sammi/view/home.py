from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
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
from ..serializers import (
    AboutImgSerializer,
    NewsSerializer,
    NewsImgSerializer,
    VideoSerializer,
    GallerySerializer,
    GalleryImgSerializer,
    VideoGallerySerializer,
    AdSerializer,
    MainStatisticSerializer,
    QuizSerializer,
    UsefulSitesSerializer,
    ContactSerializer,
)

class HomeViews(APIView):
    # @swagger_auto_schema(
    #     operation_description="Get all Home",
    #     responses={
    #         200: {
    #             "about_img": AboutImgSerializer,
    #             "news": NewsSerializer(many=True),
    #             "news_img": NewsImgSerializer(many=True),
    #             "video": VideoSerializer(many=True),
    #             "gallery": GallerySerializer(many=True),
    #             "gallery_img": GalleryImgSerializer(many=True),
    #             "video_gallery": VideoGallerySerializer(many=True),
    #             "ad": AdSerializer(many=True),
    #             "main_statistic": MainStatisticSerializer,
    #             "quiz": QuizSerializer(many=True),
    #             "useful_sites": UsefulSitesSerializer(many=True),
    #             "contact": ContactSerializer(many=True),
    #         },
    #         404: "Not Found"
    #     }
    # )
    def get(self, request: Request):
        about_img = AboutImg.objects.all()
        about_img_serializer = AboutImgSerializer(about_img, many=True).data

        news = News.objects.all()
        news_serializer = NewsSerializer(news, many=True).data
        news_data = []

        for i in news_serializer:
            news_img = NewsImg.objects.filter(news=i['id'])
            news_img_serializer = NewsImgSerializer(news_img, many=True)
            i['news_img'] = news_img_serializer.data
            news_data.append(i)

        video = Video.objects.all()
        video_serializer = VideoSerializer(video, many=True).data

        gallery = Gallery.objects.all()
        gallery_serializer = GallerySerializer(gallery, many=True).data
        gallery_data = []

        for i in gallery_serializer:
            gallery_img = GalleryImg.objects.filter(gallery=i['id'])
            gallery_img_serializer = GalleryImgSerializer(gallery_img, many=True)
            i['gallery_img'] = gallery_img_serializer.data
            gallery_data.append(i)

        video_gallery = VideoGallery.objects.all()
        video_gallery_serializer = VideoGallerySerializer(video_gallery, many=True).data

        ad = Ad.objects.all()
        ad_serializer = AdSerializer(ad, many=True).data

        main_statistic = MainStatistic.objects.all()
        main_statistic_serializer = MainStatisticSerializer(main_statistic, many=True).data

        quiz = Quiz.objects.all()
        quiz_serializer = QuizSerializer(quiz, many=True).data

        useful_sites = UsefulSites.objects.all()
        useful_sites_serializer = UsefulSitesSerializer(useful_sites, many=True).data

        contact = Contact.objects.all()
        contact_serializer = ContactSerializer(contact, many=True).data

        return Response({
            "about_img": about_img_serializer,
            "news": news_data,
            "video": video_serializer,
            "gallery": gallery_data,
            "video_gallery": video_gallery_serializer,
            "ad": ad_serializer,
            "main_statistic": main_statistic_serializer,
            "quiz": quiz_serializer,
            "useful_sites": useful_sites_serializer,
            "contact": contact_serializer,
        }, status=status.HTTP_200_OK)
    


