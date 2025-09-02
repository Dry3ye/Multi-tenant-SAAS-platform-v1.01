from django.urls import path
from .views import WelcomeMessageView

urlpatterns = [
    path('welcome-message/', WelcomeMessageView.as_view(), name='welcome-message'),
]

