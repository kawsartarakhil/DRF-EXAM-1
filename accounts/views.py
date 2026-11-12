from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serailizers import *

def tokens_for(user):
    refresh =RefreshToken.for_user(user)
    return {'refresh':str(refresh),'access':str(refresh.access_token)}

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerailizer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({'user':UserSerializer(user).data,'tokens':tokens_for(user)},status=status.HTTP_201_CREATED)


class loginView(TokenObtainPairView):
    serailizer = CustomTokenObtainedPairSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope =  'login'


@api_view(['POST'])
def logout_view(request):
    serializer = LogoutSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=status.HTTP_205_RESET_CONTENT)

@api_view(['POST'])
def change_password_view(request):
    serializer = ChangePasswordSerailizer(data=request.data,context={'request':request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'detail':'Password chnaged . Please log in again'})

