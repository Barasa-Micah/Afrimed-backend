from rest_framework import serializers
from .models import Medics

class MedicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medics
        fields = ["name", "medical_licence_number", "place_of_practice", "age"]