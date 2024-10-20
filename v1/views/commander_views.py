from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from v1.utils import process_colors
from ..serializers.commander_serializer import CommanderSerializer
from ..models.deck_model import Deck
from ..models.commander_model import Commander
import pdb


def check_for_deck_object(player_id: int, deck_id: int) -> Deck:
    try:
        Deck.objects.get(pk=deck_id, player=player_id)
    except Deck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def commander_list(request, player_id: int, deck_id: int):
    check_for_deck_object(player_id, deck_id)

    data = request.data
    colors = data.get('colors')
    color_values = process_colors(colors)

    card_data = {
        "name": data.get('name'),
        "deck": deck_id,
        "colors": color_values,
        "photo": data.get('img')
    }

    serializer = CommanderSerializer(data=card_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def commander_details(request, player_id: int, deck_id: int, commander_id: int):
    check_for_deck_object(player_id, deck_id)
    
    try:
        commander = Commander.objects.get(pk=commander_id, deck=deck_id)
    except Commander.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_commander_details(commander)
    elif request.method == 'DELETE':
        return delete_commander(commander)
    
def get_commander_details(commander: Commander):
    serializer = CommanderSerializer(commander)
    return Response(serializer.data)

def delete_commander(commander: Commander):
    commander.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
