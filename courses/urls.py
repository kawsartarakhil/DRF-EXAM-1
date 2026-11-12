from django.urls import path
from .views import *

urlpatterns = [
    path("categories/",category_list_view,name="categories"),
    path("create/",category_create_view,name="create"),
    path("update/<int:pk>/",category_update_view,name="update"),
    path("delete/<int:pk>/",category_delete_view,name="update")
]
