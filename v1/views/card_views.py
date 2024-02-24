from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..services.card_service import CardService
# from ..serializers import CardSerializer
from ..models.card_model import Card

