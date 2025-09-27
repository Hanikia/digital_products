from django.shortcuts import render
from .models import Product

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer

def home(request):
    return render(request, "home.html")

def post_list(request):
    posts = Product.objects.all()
    return render(request, "posts.html", {"posts": posts})

class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True, context = {'request' : request})
        return Response(serializer.data)
    
class ProductDetailView(APIView):

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk = pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)        
