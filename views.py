from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

# Initiate Handshake
import requests
import os
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response

load_dotenv()

@api_view(['GET'])
def initiate_handshake(request):
    url = f"{os.getenv('BASE_URL')}/initiate-handshake"

    payload = {
        "platformKey": os.getenv("PLATFORM_KEY"),
        "callbackUrl": os.getenv("CALLBACK_URL")
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        res = requests.post(url, json=payload, headers=headers)
        return Response(res.json())
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    

    
    #  Receive Callback
from .models import HandshakeToken

@api_view(['POST'])
def external_callback(request):
    token = request.data.get("handshake_token")

    if not token:
        return Response({"error": "No token received"}, status=400)

    # Save token
    HandshakeToken.objects.create(token=token)

    return Response({
        "message": "Token received successfully",
        "token": token
    })



# Complete Handshake
@api_view(['POST'])
def complete_handshake(request):
    token = request.data.get("token")

    if not token:
        return Response({"error": "Token required"}, status=400)

    url = f"{os.getenv('BASE_URL')}/complete-handshake"

    payload = {
        "platformKey": os.getenv("PLATFORM_KEY"),
        "platformSecret": os.getenv("PLATFORM_SECRET"),
        "handshakeToken": token
    }

    try:
        res = requests.post(url, json=payload)
        return Response(res.json())
    except Exception as e:
        return Response({"error": str(e)}, status=500)