from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    VideoGallery,
)
from ..serializers import (
    VideoGallerySerializer,
)

class VideoGalleryCreateView(APIView):
    @swagger_auto_schema(request_body=VideoGallerySerializer)
    def post(self, request: Request, format=None):
        serializer = VideoGallerySerializer(data=request.data)
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
    
class VideoGalleryListView(APIView):
    @swagger_auto_schema(
            responses={
                200: VideoGallerySerializer(many=True)
                }
            )
    def get(self, request: Request, format=None):
        videogallerys = VideoGallery.objects.all()
        serializer = VideoGallerySerializer(videogallerys, many=True)
        return Response(serializer.data)
    
class VideoGalleryDetailView(APIView):
    @swagger_auto_schema(
            responses={
                200: VideoGallerySerializer()
                }
            )
    def get(self, request: Request, pk, format=None):
        videogallery = VideoGallery.objects.get(pk=pk)
        serializer = VideoGallerySerializer(videogallery)
        return Response(serializer.data)
    
class VideoGalleryUpdateView(APIView):
    @swagger_auto_schema(request_body=VideoGallerySerializer)
    def put(self, request: Request, pk, format=None):
        videogallery = VideoGallery.objects.get(pk=pk)
        serializer = VideoGallerySerializer(videogallery, data=request.data)
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
    
class VideoGalleryDeleteView(APIView):
    @swagger_auto_schema(
            responses={
                204: 'No Content'
                }
            )
    def delete(self, request: Request, pk, format=None):
        videogallery = VideoGallery.objects.get(pk=pk)
        videogallery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    