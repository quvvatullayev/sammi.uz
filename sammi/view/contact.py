from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Contact,
)
from ..serializers import (
    ContactSerializer,
)

class ContactCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Create Contact",
        request_body=ContactSerializer,
        responses={
            200: ContactSerializer,
            400: "Bad Request"
        }
    )
    def post(self, request: Request):
        contact_serializer = ContactSerializer(data=request.data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return Response(contact_serializer.data, status=status.HTTP_201_CREATED)
        return Response(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContactListView(APIView):
    @swagger_auto_schema(
        operation_description="Get all Contact",
        responses={
            200: ContactSerializer(many=True),
            404: "Not Found"
        }
    )
    def get(self, request: Request):
        contact = Contact.objects.all()
        contact_serializer = ContactSerializer(contact, many=True).data
        return Response(contact_serializer, status=status.HTTP_200_OK)
    
class ContactDetailView(APIView):
    @swagger_auto_schema(
        operation_description="Get single Contact",
        responses={
            200: ContactSerializer,
            404: "Not Found"
        }
    )
    def get(self, request: Request, pk: int):
        contact = Contact.objects.get(pk=pk)
        contact_serializer = ContactSerializer(contact).data
        return Response(contact_serializer, status=status.HTTP_200_OK)
    
class ContactUpdateView(APIView):
    @swagger_auto_schema(
        operation_description="Update single Contact",
        request_body=ContactSerializer,
        responses={
            200: ContactSerializer,
            400: "Bad Request",
            404: "Not Found"
        }
    )
    def put(self, request: Request, pk: int):
        contact = Contact.objects.get(pk=pk)
        contact_serializer = ContactSerializer(contact, data=request.data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return Response(contact_serializer.data, status=status.HTTP_200_OK)
        return Response(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContactDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete single Contact",
        responses={
            200: "OK",
            404: "Not Found"
        }
    )
    def delete(self, request: Request, pk: int):
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return Response(status=status.HTTP_200_OK)
    
    
    
