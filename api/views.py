from django.shortcuts import render
from rest_framework.response import Response
from . models import Product
from . serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':

        #Get all of the produts or list of all products
        products = Product.objects.all()

        serializer = ProductSerializer(products, many = True)
        
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])   
def product(request, pk):
    try:
        product = Product.objects.get(id = pk)
    
    except Product.DoesNotExist():
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)

        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        
    if request.method == 'DELETE':
        product.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)