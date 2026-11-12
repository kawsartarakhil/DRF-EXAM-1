from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken,OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerailizer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField(required = True)
    password = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['username','email','password','password2']

    def validate_email(self,value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('This email is already registered.')
        return value.lower()

    def validate(Self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password":"Password do not match."})
        return data

    def create(self,validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id','username','email','last_login','date_joined']

class CustomTokenObtainedPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def save(self,**kwargs):
        try:
            RefreshToken(self.validated_data['refresh']).blacklist()
        except TokenError:
            raise serializers.ValidationError({'refresh':'Token is invalid pr expired'})

class ChangePasswordSerailizer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True,validators=[validate_password])

    def validate_old_password(self,value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('old password is incorrect')
        return value

    def save(self,**kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        for token in OutstandingToken.objects.filter(user=user):
            BlacklistedToken.objects.get_or_create(token=token)
        return user