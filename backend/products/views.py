from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, ProductImage
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response({'message': 'Category deleted successfully'},status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search = request.GET.get('search')
        category = request.GET.get('category')
        if search:
            products = products.filter(name__icontains=search)
        if category:
            products = products.filter(category_id=category)
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(
            {'error': 'Product not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(
            product,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'DELETE':
        product.delete()
        return Response(
            {'message': 'Product deleted successfully'},
            status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def product_image_list(request):

    if request.method == 'GET':

        images = ProductImage.objects.all()

        serializer = ProductImageSerializer(
            images,
            many=True
        )

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = ProductImageSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
def product_image_delete(request, pk):

    try:
        image = ProductImage.objects.get(pk=pk)

    except ProductImage.DoesNotExist:

        return Response(
            {'error': 'Image not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    image.delete()

    return Response(
        {'message': 'Image deleted successfully'},
        status=status.HTTP_204_NO_CONTENT
    )