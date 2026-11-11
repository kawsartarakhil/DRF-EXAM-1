from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view,permission_classes
from .serailizers import *

# @api_view(["GET"])
# def category_list_view(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

# @api_view(["POST"])
# def category_create_view(request):
#     serializer = CategorySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


