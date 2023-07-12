from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    GalleryImg,
)
from ..serializers import (
    GalleryImgSerializer,
)

class GalleryImgCreateView(APIView):
    @swagger_auto_schema(request_body=GalleryImgSerializer)
    def post(self, request: Request, format=None):
        serializer = GalleryImgSerializer(data=request.data)
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

class GalleryImgListView(APIView):
    @swagger_auto_schema(
            responses={
                200: GalleryImgSerializer(many=True)
                }
            )
    def get(self, request: Request, format=None):
        galleryimgs = GalleryImg.objects.all()
        serializer = GalleryImgSerializer(galleryimgs, many=True)
        return Response(serializer.data)
    
class GalleryImgDetailView(APIView):
    @swagger_auto_schema(
            responses={
                200: GalleryImgSerializer()
                }
            )
    def get(self, request: Request, pk, format=None):
        galleryimg = GalleryImg.objects.get(pk=pk)
        serializer = GalleryImgSerializer(galleryimg)
        return Response(serializer.data)
    
class GalleryImgUpdateView(APIView):
    @swagger_auto_schema(request_body=GalleryImgSerializer)
    def put(self, request: Request, pk, format=None):
        galleryimg = GalleryImg.objects.get(pk=pk)
        serializer = GalleryImgSerializer(galleryimg, data=request.data)
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
    
class GalleryImgDeleteView(APIView):
    def delete(self, request: Request, pk, format=None):
        galleryimg = GalleryImg.objects.get(pk=pk)
        galleryimg.delete()
        return Response(
            {
                'message': 'galleryimg deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )
    
    
        
    