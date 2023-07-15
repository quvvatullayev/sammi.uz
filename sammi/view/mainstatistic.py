from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    MainStatistic,
)
from ..serializers import (
    MainStatisticSerializer,
)

class MainStatisticCreateViews(APIView):
    @swagger_auto_schema(
        request_body=MainStatisticSerializer,
        operation_description="Create MainStatistic",
        responses={
            201: MainStatisticSerializer,
            400: "Bad Request"
        }
    )
    def post(self, request: Request):
        serializer = MainStatisticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MainStatisticDetailViews(APIView):
    @swagger_auto_schema(
        operation_description="Get MainStatistic by id",
        responses={
            200: MainStatisticSerializer,
            404: "Not Found"
        }
    )
    def get(self, request: Request, pk: int):
        try:
            mainstatistic = MainStatistic.objects.get(pk=pk)
        except MainStatistic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MainStatisticSerializer(mainstatistic)
        return Response(serializer.data)
    
class MainStatisticListViews(APIView):
    @swagger_auto_schema(
        operation_description="Get all MainStatistic",
        responses={
            200: MainStatisticSerializer(many=True),
            404: "Not Found"
        }
    )
    def get(self, request: Request):
        mainstatistic = MainStatistic.objects.all()
        serializer = MainStatisticSerializer(mainstatistic, many=True)
        return Response(serializer.data)
    
class MainStatisticUpdateViews(APIView):
    @swagger_auto_schema(
        operation_description="Update MainStatistic by id",
        responses={
            200: MainStatisticSerializer,
            404: "Not Found"
        }
    )
    def put(self, request: Request, pk: int):
        try:
            mainstatistic = MainStatistic.objects.get(pk=pk)
        except MainStatistic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MainStatisticSerializer(mainstatistic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
class MainStatisticDeleteViews(APIView):
    @swagger_auto_schema(
        operation_description="Delete MainStatistic by id",
        responses={
            204: "No Content",
            404: "Not Found"
        }
    )
    def delete(self, request: Request, pk: int):
        try:
            mainstatistic = MainStatistic.objects.get(pk=pk)
        except MainStatistic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        mainstatistic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    