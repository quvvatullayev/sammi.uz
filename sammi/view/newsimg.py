from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    News,
    NewsImg,
)
from ..serializer import (
    NewsSerializer,
    NewsImgSerializer,
)

class NewsImgCreateView(APIView):
    @swagger_auto_schema(request_body=NewsImgSerializer)
    def post(self, request: Request, format=None):
        serializer = NewsImgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {
                'message': 'invalid data',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
class NewsImgListView(APIView):
    @swagger_auto_schema(
            responses={
                200: NewsImgSerializer(many=True)
                }
            )
    def get(self, request: Request, format=None):
        newsimgs = NewsImg.objects.all()
        serializer = NewsImgSerializer(newsimgs, many=True)
        return Response(serializer.data)
    
class NewsImgDetailView(APIView):
    @swagger_auto_schema(
            responses={
                200: NewsImgSerializer()
                }
            )
    def get(self, request: Request, pk, format=None):
        newsimg = NewsImg.objects.get(pk=pk)
        serializer = NewsImgSerializer(newsimg)
        return Response(serializer.data)

class NewsImgUpdateView(APIView):
    @swagger_auto_schema(request_body=NewsImgSerializer)
    def put(self, request: Request, pk, format=None):
        newsimg = NewsImg.objects.get(pk=pk)
        serializer = NewsImgSerializer(newsimg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            {
                'message': 'invalid data',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
class NewsImgDeleteView(APIView):
    def delete(self, request: Request, pk, format=None):
        newsimg = NewsImg.objects.get(pk=pk)
        newsimg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

        
        
        
    