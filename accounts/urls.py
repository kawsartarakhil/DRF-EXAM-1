from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView
from .views import *

urlpatterns = [
    path("register/",register_view,name="register"),
    path("login/",loginView,name="login"),
    path("refresh/",TokenRefreshView.as_view(),name="refresh"),
    path("logout/",logout_view,name="logout"),
    path("change_password",change_password_view,name="change_password")
]
