from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.deck_serializer import DeckSerializer
from ..serializers.commander_serializer import CommanderSerializer
from ..models.deck_model import Deck
from ..models.commander_model import Commander

@api_view(['GET', 'POST'])
def commander_list(request, deck_id):
    try:
        check_for_deck = Deck.objects.get(pk=deck_id)
    except Deck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return get_commander_list(request, check_for_deck)
    elif request.method == 'POST':
        return create_commander(request)
    
def get_commander_list(request, check_for_deck):
  commanders = Commander.objects.filter(deck=check_for_deck)
  serializer = CommanderSerializer(commanders, many=True)
  return Response(serializer.data)

def create_commander(request):
  serializer = CommanderSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def commander_details(request, deck_id, commander_id):
  try:
    deck = Deck.objects.get(pk=deck_id)
  except Deck.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  try:
    commander = Commander.objects.get(pk=commander_id, deck=deck)
  except Commander.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    return get_commander_details(commander)
  elif request.method == 'PUT':
    return update_commander(commander, request.data)
  elif request.method == 'DELETE':
    return delete_commander(commander)
  
def get_commander_details(commander):
  serializer = CommanderSerializer(commander)
  return Response(serializer.data)

def update_commander(commander, data):
  commander_data = CommanderSerializer(commander, data=data, partial=True)
  if commander_data.is_valid():
    commander_data.save()
    return Response(commander_data.data)
  return Response(status=status.HTTP_400_BAD_REQUEST)

def delete_commander(commander):
  commander.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)