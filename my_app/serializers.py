from rest_framework import serializers
from .models import *


class DarajaSerializer(serializers.ModelSerializer):
    class Meta:
        models = Daraja
        fields = '__all__'
