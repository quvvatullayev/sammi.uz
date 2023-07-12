from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Gallery,
)
from ..serializer import (
    GallerySerializer,
)

class GalleryCreateView(APIView):
    @swagger_auto_schema(request_body=GallerySerializer)
    def post(self, request: Request, format=None):
        serializer = GallerySerializer(data=request.data)
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
    
class GalleryListView(APIView):
    @swagger_auto_schema(
            responses={
                200: GallerySerializer(many=True)
                }
            )
    def get(self, request: Request, format=None):
        gallerys = Gallery.objects.all()
        serializer = GallerySerializer(gallerys, many=True)
        return Response(serializer.data)
    
class GalleryDetailView(APIView):
    @swagger_auto_schema(
            responses={
                200: GallerySerializer()
                }
            )
    def get(self, request: Request, pk, format=None):
        gallery = Gallery.objects.get(pk=pk)
        serializer = GallerySerializer(gallery)
        return Response(serializer.data)
    
class GalleryUpdateView(APIView):
    @swagger_auto_schema(request_body=GallerySerializer)
    def put(self, request: Request, pk, format=None):
        gallery = Gallery.objects.get(pk=pk)
        serializer = GallerySerializer(gallery, data=request.data)
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
    
class GalleryDeleteView(APIView):
    @swagger_auto_schema(
            responses={
                200: GallerySerializer()
                }
            )
    def delete(self, request: Request, pk, format=None):
        gallery = Gallery.objects.get(pk=pk)
        gallery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    
    
