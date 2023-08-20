from django.urls import path
from main.views import WebhookAPIView, McDonaldCuponGenAPIView

urlpatterns = [
    path('webhook/', WebhookAPIView.as_view(), name='webhook'),
    path('mc/', McDonaldCuponGenAPIView.as_view(), name='mc')
]
