from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.game_serializer import GameSerializer
from ..models.pod_model import Pod
from ..models.game_model import Game


OPTIONAL_FIELDS = ["total_turns", "game_log"]

@api_view(['GET', 'POST'])
def game_list(request, pod_id: int):
    try:
        checked_pod = Pod.objects.get(pk=pod_id)
    except Pod.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_game_list(checked_pod)
    elif request.method == 'POST':
        return create_game(request.data, pod_id)

def get_game_list(checked_pod: Pod):
    games = Game.objects.filter(pod=checked_pod)
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

def create_game(data: dict, pod_id: int):

    new_game_data = {
        "pod": pod_id
    }

    for field in OPTIONAL_FIELDS:
        if field in data:
            new_game_data[field] = data[field]

    serializer = GameSerializer(data=new_game_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def game_details(request, game_id: int, pod_id: int):
    try:
        game = Game.objects.get(pk=game_id, pod=pod_id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_game_details(game)
    elif request.method == 'PUT':
        return update_game(game, request.data)
    elif request.method == 'DELETE':
        return delete_game(game)

def get_game_details(game: Game):
    serializer = GameSerializer(game)
    return Response(serializer.data)

def update_game(game: Game, data: dict):
    updated_data = {}
    for field in OPTIONAL_FIELDS:
        if field in data:
            updated_data[field] = data[field]

    game_data = GameSerializer(game, data=updated_data, partial=True)
    if game_data.is_valid():
        game_data.save()
        return Response(game_data.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

def delete_game(game: Game):
    game.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
