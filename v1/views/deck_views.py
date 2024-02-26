from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.deck_serializer import DeckSerializer
from ..serializers.player_serializer import PlayerSerializer
# from ..serializers.commander_serializer import CommanderSerializer
from ..models.deck_model import Deck
from ..models.player_model import Player
# from ..models.commander_model import Commander

@api_view(['GET', 'POST'])
def deck_list(request, player_id):
    try:
        check_for_player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_deck_list(request, check_for_player)
    elif request.method == 'POST':
        return create_deck(request)
    
def get_deck_list(request, check_for_player):
    decks = Deck.objects.filter(player=check_for_player)
    serializer = DeckSerializer(decks, many=True)
    return Response(serializer.data)

def create_deck(request):
    serializer = DeckSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def deck_details(request, deck_id, player_id):
    try:
        player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    try:
        deck = Deck.objects.get(pk=deck_id)
    except Deck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_deck_details(deck)
    elif request.method == 'PUT':
        return update_deck(deck, request.data)
    elif request.method == 'DELETE':
        return delete_deck(deck)
    
def get_deck_details(deck):
    serializer = DeckSerializer(deck)
    return Response(serializer.data)

def update_deck(deck, data):
    deck_data = DeckSerializer(deck, data=data, partial=True)
    if deck_data.is_valid():
        deck_data.save()
        return Response(deck_data.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

def delete_deck(deck):
    deck.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)