from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from ..serializers import (
    UserSerializer,
)

class UserCreateView(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            status.HTTP_201_CREATED: UserSerializer,
            status.HTTP_400_BAD_REQUEST: 'Bad Request',
        },
    )
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response(
                {
                    'user': serializer.data,
                    'token': token.key,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            status.HTTP_200_OK: UserSerializer,
            status.HTTP_400_BAD_REQUEST: 'Bad Request',
        },
    )
    def post(self, request:Request) -> Response:
        user = request.user
        token = Token.objects.create(user=user)
        return Response(
            {
                'user': UserSerializer(user).data,
                'token': token.key,
            },
            status=status.HTTP_200_OK,
        )
    
class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request:Request) -> Response:
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserCreateAdminView(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request:Request, pk:int) -> Response:
        if request.user.is_superuser:
            user = User.objects.get(pk=pk)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
class UserDeleteAdminView(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request:Request, pk:int) -> Response:
        if request.user.is_superuser:
            user = User.objects.get(pk=pk)
            user.is_staff = False
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
class UserAdminListView(APIView):
    authentication_classes = [TokenAuthentication]
    def get(self, request:Request) -> Response:
        if request.user.is_superuser:
            users = User.objects.all()
            return Response(
                {
                    'users': UserSerializer(users, many=True).data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
class UserNontAdminListView(APIView):
    authentication_classes = [TokenAuthentication]
    def get(self, request:Request) -> Response:
        if request.user.is_superuser:
            users = User.objects.filter(is_staff=False)
            return Response(
                {
                    'users': UserSerializer(users, many=True).data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
