from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view,permission_classes
from .serailizers import *
from rest_framework.response import Response
from rest_framework.exceptions import status

@api_view(["GET"])
def category_list_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        name =request.query_params.get("name")
        if name:
            categories = categories.filter(name__icontains=name)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_category(request,pk):
    if request.method == 'GET':
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    return Response({"error":"category not found"},status=status.HTTP_404_NOT_FOUND)
    

@api_view(["POST"])
def category_create_view(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def category_update_view(request,pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"error":"Catergory not found"},status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PUT":
        serializer = CategorySerializer(category,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def category_delete_view(request,pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"error":"Category Not found"})
    category.delete()
    return Response({"message": "Category deleted"})     





@api_view(["GET"])
def course_list_view(request):
    if request.method == 'GET':
        courses = Courses.objects.all()
        title =request.query_params.get("name")
        if title:
            courses = courses.filter(title__icontains=title)

        min_price = request.query_params.get("min_price")
        if min_price:
            courses = courses.filter(price__gte=min_price)

        max_price = request.query_params.get("max_price")
        if max_price:
            courses = courses.filter(price__lte=max_price)

        ordering = request.query_params.get("ordering")
        if ordering in ["price", "-price","title", "-title"]:
            courses = courses.order_by(ordering)

        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_course(request,pk):
    if request.method == 'GET':
        courses = Courses.objects.get(pk=pk)
        serializer = CoursesSerializer(courses,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    return Response({"error":"course not found"},status=status.HTTP_404_NOT_FOUND)
    

@api_view(["POST"])
def course_create_view(request):
    serializer = CoursesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def course_update_view(request,pk):
    try:
        courses = Courses.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"error":"course not found"},status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PUT":
        serializer = CoursesSerializer(courses,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def course_delete_view(request,pk):
    try:
        courses = Courses.objects.get(pk=pk)
    except Courses.DoesNotExist:
        return Response({"error":"courses Not found"})
    courses.delete()
    return Response({"message": "courses deleted"}) 
    


