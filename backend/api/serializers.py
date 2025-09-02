from rest_framework import serializers
from .models import WelcomeMessage

class WelcomeMessageSerializer(serializers.ModelSerializer):
    """Serializer for the WelcomeMessage model."""
    class Meta:
        model = WelcomeMessage
        fields = ['message']
