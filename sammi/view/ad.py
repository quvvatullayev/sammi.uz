from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Ad,
)
from ..serializers import (
    AdSerializer,
)

class AdCreateView(APIView):
    @swagger_auto_schema(request_body=AdSerializer)
    def post(self, request: Request, format=None):
        serializer = AdSerializer(data=request.data)
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
    
class AdListView(APIView):
    @swagger_auto_schema(
            responses={
                200: AdSerializer(many=True)
                }
            )
    def get(self, request: Request, format=None):
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data)
    
class AdDetailView(APIView):
    @swagger_auto_schema(
            responses={
                200: AdSerializer()
                }
            )
    def get(self, request: Request, pk, format=None):
        ad = Ad.objects.get(pk=pk)
        serializer = AdSerializer(ad)
        return Response(serializer.data)
    
class AdUpdateView(APIView):
    @swagger_auto_schema(request_body=AdSerializer)
    def put(self, request: Request, pk, format=None):
        ad = Ad.objects.get(pk=pk)
        serializer = AdSerializer(ad, data=request.data)
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
    
class AdDeleteView(APIView):
    @swagger_auto_schema(
            responses={
                204: None
                }
            )
    def delete(self, request: Request, pk, format=None):
        ad = Ad.objects.get(pk=pk)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)