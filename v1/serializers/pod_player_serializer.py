from rest_framework import serializers
from ..models.pod_player_model import PodPlayer

class PodPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodPlayer
        fields = ['id', 'player', 'pod', 'total_games', 'total_wins', 'games_as_archenemy', 'wins_as_archenemy', 'total_kills', 'created_at', 'updated_at']