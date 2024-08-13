from django.http import JsonResponse
from typing import Optional
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.pod_player_serializer import PodPlayerSerializer
from ..models.player_model import Player
from ..models.pod_model import Pod
from ..models.pod_player_model import PodPlayer


# Pods by Player
@api_view(['GET', 'POST'])
def pods_by_player_list(request, player_id: int):
    try:
        player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        return Response({"error": "Player not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_pod_player_list(player)
    elif request.method == 'POST':
        return create_pod_player(request.data, player)

def get_pod_player_list(player: Player):
    pod_players = PodPlayer.objects.filter(player=player)
    serializer = PodPlayerSerializer(pod_players, many=True)
    return Response(serializer.data)

def create_pod_player(data, player: Player):
    new_pod_player_data = {
        "player": player.id,
        "pod": data["pod"]
    }

    serializer = PodPlayerSerializer(data=new_pod_player_data)
    if serializer.is_valid():
        player_id = serializer.validated_data['player']
        pod_id = serializer.validated_data['pod']

        if PodPlayer.objects.filter(player=player_id, pod=pod_id).exists():
            return Response({"error": "PodPlayer association already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def pod_by_player_details(request, player_id: int, pod_id: int):
    try:
        check_player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        return Response({"error": "Player not found."}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        check_pod = Pod.objects.get(pk=pod_id)
    except Pod.DoesNotExist:
        return Response({"error": "Pod not found."}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        check_pod_player = PodPlayer.objects.get(player=check_player, pod=check_pod)
    except PodPlayer.DoesNotExist:
        return Response({"error": "PodPlayer not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_pod_player(check_pod_player)
    elif request.method == 'DELETE':
        return delete_pod_player(check_pod_player)

def get_pod_player(check_pod_player: PodPlayer):
    serializer = PodPlayerSerializer(check_pod_player)
    return Response(serializer.data)

def delete_pod_player(check_pod_player: PodPlayer):
    check_pod_player.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Players by Pod
@api_view(['GET'])
def players_by_pod(request, pod_id: int, player_id: Optional[int] = None):
    try:
        Pod.objects.get(pk=pod_id)
    except Pod.DoesNotExist:
        return Response({"error": "Pod not found."}, status=status.HTTP_404_NOT_FOUND)    
    
    if player_id is None:
        return get_all_players_by_pod(pod_id)
    else:
        return get_specific_player_by_pod(pod_id, player_id)
    
def get_all_players_by_pod(pod_id: int):
    pod_players = PodPlayer.objects.filter(pod=pod_id)
    serializer = PodPlayerSerializer(pod_players, many=True)
    return Response(serializer.data)

def get_specific_player_by_pod(pod_id: int, player_id: int):
    try:
        pod_player = PodPlayer.objects.get(player=player_id, pod=pod_id)
    except PodPlayer.DoesNotExist:
        return Response({"error": "PodPlayer not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = PodPlayerSerializer(pod_player)
    return Response(serializer.data)
