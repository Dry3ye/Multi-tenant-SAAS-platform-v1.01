from django.db import models

class WelcomeMessage(models.Model):
    """A model to hold a welcome message for a tenant."""
    message = models.CharField(max_length=255)
    
    def __str__(self):
        return self.message

