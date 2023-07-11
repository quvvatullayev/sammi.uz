from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    AboutImg,
)
from ..serializer import (
    AboutImgSerializer,
)

class AboutImgCreateView(APIView):
    def post(self, request: Request, format=None):
        serializer = AboutImgSerializer(data=request.data)
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
    
class AboutImgListView(APIView):
    def get(self, request: Request, format=None):
        aboutimgs = AboutImg.objects.all()
        serializer = AboutImgSerializer(aboutimgs, many=True)
        return Response(serializer.data)

class AboutImgDetailView(APIView):
    def get(self, request: Request, pk, format=None):
        aboutimg = AboutImg.objects.get(pk=pk)
        serializer = AboutImgSerializer(aboutimg)
        return Response(serializer.data)
    
class AboutImgUpdateView(APIView):
    def put(self, request: Request, pk, format=None):
        aboutimg = AboutImg.objects.get(pk=pk)
        serializer = AboutImgSerializer(aboutimg, data=request.data)
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
    
class AboutImgDeleteView(APIView):
    def delete(self, request: Request, pk, format=None):
        aboutimg = AboutImg.objects.get(pk=pk)
        aboutimg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)