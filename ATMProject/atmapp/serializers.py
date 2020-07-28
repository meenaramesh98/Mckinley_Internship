from rest_framework import serializers
from .models import AtmPinRegister

class AtmPinRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtmPinRegister
        fields = '__all__'