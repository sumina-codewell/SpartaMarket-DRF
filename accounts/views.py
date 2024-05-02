from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import MyUser
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import JoinSerializer, UsernameSerializer

# Create your views here.
class Join(APIView):
    def post(self, request):
        serializer = JoinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(raise_exception=True)
            return Response(serializer.data, status=201)
        
class Username(APIView):
    def get(self, request):
        userinfo = MyUser.objects.all()
        serializer = UsernameSerializer(userinfo)
        return Response(serializer.data)