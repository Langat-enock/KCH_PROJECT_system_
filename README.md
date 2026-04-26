# KCH_PROJECT_system_
AfyaAnalytics Handshake Integration

This project implements a secure external platform that integrates with the AfyaAnalytics Health Platform using a two-step handshake authentication flow. Built with Django and Django REST Framework, the system initiates a handshake request, receives a callback containing a handshake token, and completes authentication within the required time window.

**Features**
Initiates handshake with AfyaAnalytics API
Receives and stores handshake token securely
Completes authentication flow using platform credentials
Uses environment variables for sensitive data
RESTful API endpoints for testing with Postman
Basic error handling and token management

**Installation**
fire up this coomand  "pip install python-dotenv requests djangorestframework"   to install python-dotenv, requests and djangorestframework packages  need to import os and load_dotenv to read environment variables from .env file in settings.py file
 add enviroment varable  to seting.py file that is " BASE_URL = os.getenv("BASE_URL")" and "PLATFORM_KEY = os.getenv("PLATFORM_KEY")" and "CALLBACK_URL = os.getenv("CALLBACK_URL")" to read the values from .env file
RSET Framework configuration to allow any permission for API views in settings.py file

**Django Settings (settings.py)**

Import and load environment variables:

import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
PLATFORM_KEY = os.getenv("PLATFORM_KEY")
CALLBACK_URL = os.getenv("CALLBACK_URL")

**Configure Django REST Framework:**
by writing tis code in setteting.py

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

**fire migration command **
python manage.py makemigrations
python manage.py migrate
