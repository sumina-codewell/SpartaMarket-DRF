from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Product
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Product(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        permission_classes = [IsAuthenticated]
        
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(raise_exception=True)
            return Response(serializer.data, status=201)