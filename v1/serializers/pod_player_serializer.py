from rest_framework import serializers
from ..models.pod_player_model import PodPlayer

class PodPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodPlayer
        fields = ['id', 'player', 'pod', 'total_wins', 'total_games', 'total_win_percentage', 'total_kills' 'kill_average', 'games_as_archenemy', 'wins_as_archenemy', 'created_at' 'updated_at']