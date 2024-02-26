from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.player_serializer import PlayerSerializer
from ..models.player_model import Player

@api_view(['GET', 'POST'])
def player_list(request):
    if request.method == 'GET':
        return get_player_list(request)
    elif request.method == 'POST':
        return create_player(request)
    
def get_player_list(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)

def create_player(request):
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def player_details(request, player_id):
    try:
        player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_specific_player(player)
    elif request.method == 'PUT':
        return update_specific_player(player, request)
    elif request.method == 'DELETE':
        return delete_player(player)
    
def get_specific_player(player):
    serializer = PlayerSerializer(player)
    return Response(serializer.data)

def update_specific_player(player, request):
    player_data = PlayerSerializer(player, data=request.data, partial=True)
    if player_data.is_valid():
        player_data.save()
        return Response(player_data.data)
    return Response(player_data.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_player(player):
    player.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)