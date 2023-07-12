from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Video,
)
from ..serializer import (
    VideoSerializer,
)

class VideoCreateView(APIView):
    @swagger_auto_schema(request_body=VideoSerializer)
    def post(self, request: Request, format=None):
        serializer = VideoSerializer(data=request.data)
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


class VideoListView(APIView):
    @swagger_auto_schema(
            responses={
                200: VideoSerializer(many=True)
                }
            )
    def get(self, request: Request, format=None):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    
class VideoDetailView(APIView):
    @swagger_auto_schema(
            responses={
                200: VideoSerializer()
                }
            )
    def get(self, request: Request, pk, format=None):
        video = Video.objects.get(pk=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)
    
class VideoUpdateView(APIView):
    @swagger_auto_schema(request_body=VideoSerializer)
    def put(self, request: Request, pk, format=None):
        video = Video.objects.get(pk=pk)
        serializer = VideoSerializer(video, data=request.data)
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
    
class VideoDeleteView(APIView):
    def delete(self, request: Request, pk, format=None):
        video = Video.objects.get(pk=pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
        
        
        
        
        
        
    