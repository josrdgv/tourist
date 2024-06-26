from .models import tour_destinations
from rest_framework import serializers

class tourist_serializer(serializers.ModelSerializer):
    destination_img=serializers.ImageField(required=False)

    class Meta:
        model=tour_destinations
        fields='__all__'
