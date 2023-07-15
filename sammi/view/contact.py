from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    UsefulSites,
)
from ..serializers import (
    UsefulSitesSerializer,
)

class UsefulSitesCreateViews(APIView):
    @swagger_auto_schema(
        request_body=UsefulSitesSerializer,
        operation_description="Create UsefulSites",
        responses={
            201: UsefulSitesSerializer,
            400: "Bad Request"
        }
    )
    def post(self, request: Request):
        serializer = UsefulSitesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UsefulSitesDetailViews(APIView):
    @swagger_auto_schema(
        operation_description="Get UsefulSites by id",
        responses={
            200: UsefulSitesSerializer,
            404: "Not Found"
        }
    )
    def get(self, request: Request, pk: int):
        try:
            usefulsites = UsefulSites.objects.get(pk=pk)
        except UsefulSites.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UsefulSitesSerializer(usefulsites)
        return Response(serializer.data)
    
class UsefulSitesListViews(APIView):
    @swagger_auto_schema(
        operation_description="Get all UsefulSites",
        responses={
            200: UsefulSitesSerializer(many=True),
            404: "Not Found"
        }
    )
    def get(self, request: Request):
        usefulsites = UsefulSites.objects.all()
        serializer = UsefulSitesSerializer(usefulsites, many=True)
        return Response(serializer.data)
    
class UsefulSitesUpdateViews(APIView):
    @swagger_auto_schema(
        request_body=UsefulSitesSerializer,
        operation_description="Update UsefulSites by id",
        responses={
            200: UsefulSitesSerializer,
            404: "Not Found"
        }
    )
    def put(self, request: Request, pk: int):
        try:
            usefulsites = UsefulSites.objects.get(pk=pk)
        except UsefulSites.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UsefulSitesSerializer(usefulsites, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UsefulSitesDeleteViews(APIView):
    @swagger_auto_schema(
        operation_description="Delete UsefulSites by id",
        responses={
            204: "No Content",
            404: "Not Found"
        }
    )
    def delete(self, request: Request, pk: int):
        try:
            usefulsites = UsefulSites.objects.get(pk=pk)
        except UsefulSites.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        usefulsites.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
