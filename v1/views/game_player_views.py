from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.game_player_serializer import GamePlayerSerializer
from ..models.game_model import Game
from ..models.game_player_model import GamePlayer
import pdb


OPTIONAL_FIELDS = ["is_winner", "is_archenemy", "kills"]

@api_view(['GET', 'POST'])
def game_player_list(request, game_id: int):
    try:
        checked_game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        print("hello there")
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_game_player_list(checked_game)
    elif request.method == 'POST':
        return create_game_player(request.data, checked_game)

def get_game_player_list(checked_game: Game):
    game_players = GamePlayer.objects.filter(game=checked_game)
    serializer = GamePlayerSerializer(game_players, many=True)
    return Response(serializer.data)

def create_game_player(data: dict, game: Game):
    new_game_player_data = {
        "game": game.id,
        "player": data["player"],
        "deck": data["deck"],
    }

    for field in OPTIONAL_FIELDS:
        if field in data:
            new_game_player_data[field] = data[field]

    serializer = GamePlayerSerializer(data=new_game_player_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def game_player_details(request, game_id: int, game_player_id: int):
    try:
        Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    try:
        game_player = GamePlayer.objects.get(pk=game_player_id)
    except GamePlayer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_game_player_details(game_player)
    elif request.method == 'PUT':
        return update_game_player(game_player, request.data)
    elif request.method == 'DELETE':
        return delete_game_player(game_player)

def get_game_player_details(game_player: GamePlayer):
    serializer = GamePlayerSerializer(game_player)
    return Response(serializer.data)

def update_game_player(game_player: GamePlayer, data: dict):
    updated_data = {}
    for field in OPTIONAL_FIELDS:
        if field in data:
            updated_data[field] = data[field]
    
    game_player_data = GamePlayerSerializer(game_player, data=updated_data, partial=True)
    if game_player_data.is_valid():
        game_player_data.save()
        return Response(game_player_data.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

def delete_game_player(game_player: GamePlayer):
    game_player.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
