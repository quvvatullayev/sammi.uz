from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    News,
)
from ..serializers import (
    NewsSerializer,
)

class NewsCreateView(APIView):
    @swagger_auto_schema(request_body=NewsSerializer)
    def post(self, request: Request, format=None):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'news created successfully',
                    'news': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'message': 'invalid data',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
class NewsListView(APIView):
    @swagger_auto_schema(
            responses={
                200: NewsSerializer(many=True)
                }
            )
    def get(self, request: Request, format=None):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
    
class NewsDetailView(APIView):
    @swagger_auto_schema(
            responses={
                200: NewsSerializer()
                }
            )
    def get(self, request: Request, pk, format=None):
        news = News.objects.get(pk=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)
    
class NewsUpdateView(APIView):
    @swagger_auto_schema(request_body=NewsSerializer)
    def put(self, request: Request, pk, format=None):
        news = News.objects.get(pk=pk)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'news updated successfully',
                    'news': serializer.data
                }
            )
        return Response(
            {
                'message': 'invalid data',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
class NewsDeleteView(APIView):
    def delete(self, request: Request, pk, format=None):
        news = News.objects.get(pk=pk)
        news.delete()
        return Response(
            {
                'message': 'news deleted successfully',
            }
        )
