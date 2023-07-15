from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Quiz,
)
from ..serializers import (
    QuizSerializer,
)

class QuizCreateViews(APIView):
    @swagger_auto_schema(
        request_body=QuizSerializer,
        operation_description="Create Quiz",
        responses={
            201: QuizSerializer,
            400: "Bad Request"
        }
    )
    def post(self, request: Request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuizDetailViews(APIView):
    @swagger_auto_schema(
        operation_description="Get Quiz by id",
        responses={
            200: QuizSerializer,
            404: "Not Found"
        }
    )
    def get(self, request: Request, pk: int):
        try:
            quiz = Quiz.objects.get(pk=pk)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)
    
class QuizListViews(APIView):
    @swagger_auto_schema(
        operation_description="Get all Quiz",
        responses={
            200: QuizSerializer(many=True),
            404: "Not Found"
        }
    )
    def get(self, request: Request):
        quiz = Quiz.objects.all()
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)
    
class QuizUpdateViews(APIView):
    @swagger_auto_schema(
        request_body=QuizSerializer,
        operation_description="Update Quiz by id",
        responses={
            200: QuizSerializer,
            404: "Not Found"
        }
    )
    def put(self, request: Request, pk: int):
        try:
            quiz = Quiz.objects.get(pk=pk)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuizDeleteViews(APIView):
    @swagger_auto_schema(
        operation_description="Delete Quiz by id",
        responses={
            204: "No Content",
            404: "Not Found"
        }
    )
    def delete(self, request: Request, pk: int):
        try:
            quiz = Quiz.objects.get(pk=pk)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    
    
    