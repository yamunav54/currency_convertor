from rest_framework import serializers
from .models import RateList

class RateListSerializer(serializers.ModelSerializer):
    class Meta:
        model= RateList
        fields = ['id','flat_currency','variable_currency','rate']

class FlatCurListSerializer(serializers.ModelSerializer):
    class Meta:
        model= RateList
        fields = ['flat_currency']

class VarCurListSerializer(serializers.ModelSerializer):
    class Meta:
        model= RateList
        fields = ['variable_currency']

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model= RateList
        fields = ['rate']