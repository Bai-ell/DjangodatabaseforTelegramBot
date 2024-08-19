from rest_framework import serializers
from .models import Links, Contats

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'

class ContatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contats
        fields = '__all__'
