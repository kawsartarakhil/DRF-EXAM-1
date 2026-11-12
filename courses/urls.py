from django.urls import path
from .views import *

urlpatterns = [
    path("categories/",category_list_view,name="categories"),
    path("category/",get_category,name="category"),
    path("create/",category_create_view,name="create"),
    path("update/<int:pk>/",category_update_view,name="update"),
    path("delete/<int:pk>/",category_delete_view,name="update"),



    path("courses/",course_list_view,name="categories"),
    path("course/",get_course,name="category"),
    path("create_course/",course_create_view,name="create"),
    path("update_course/<int:pk>/",course_update_view,name="update"),
    path("delete-course/<int:pk>/",course_delete_view,name="update"),
]
