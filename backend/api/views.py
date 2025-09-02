from rest_framework import generics
from .models import WelcomeMessage
from .serializers import WelcomeMessageSerializer

class WelcomeMessageView(generics.RetrieveAPIView):
    """API view to retrieve the welcome message for the current tenant."""
    queryset = WelcomeMessage.objects.all()
    serializer_class = WelcomeMessageSerializer
    lookup_field = 'pk'
    
    def get_object(self):
        # We'll just return the first object in the schema for now
        return self.get_queryset().first()
