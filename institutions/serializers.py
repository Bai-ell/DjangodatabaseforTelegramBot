from rest_framework import serializers
from .models import Institution, Mta, ShortNamesMta




class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = '__all__'

class MtaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mta
        fields = '__all__'



class ShortNamesMtaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortNamesMta
        fields = '__all__'