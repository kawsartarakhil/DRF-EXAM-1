from rest_framework import serializers
from .models import Catergories

class CatergorySerailizer(serializers.BaseSerializer):
    class Meta:
        model = Catergories
        fields = ["name","description"]
