from django.urls import path
from .views import google_auth_redirect, google_auth_callback

urlpatterns = [
    path('google/', google_auth_redirect),
    path('callback/', google_auth_callback),
]
