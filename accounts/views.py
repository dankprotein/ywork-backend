from django.shortcuts import render

import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def google_auth_redirect(request):
    url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        "?client_id={}&response_type=code"
        "&scope=email%20profile"
        "&redirect_uri={}"
    ).format(settings.GOOGLE_CLIENT_ID, settings.GOOGLE_REDIRECT_URI)
    return Response({"auth_url": url})


@api_view(['GET'])
def google_auth_callback(request):
    code = request.GET.get("code")
    if not code:
        return Response({"error": "Missing code"}, status=400)

    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    response = requests.post(token_url, data=data)
    if response.status_code != 200:
        return Response({"error": "Token exchange failed"}, status=400)

    return Response(response.json())

