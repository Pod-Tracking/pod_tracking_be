from rest_framework import serializers
from ..models.player_model import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'photo', 'email', 'password', 'total_games', 'total_wins', 'games_as_archenemy', 'wins_as_archenemy', 'total_kills', 'created_at', 'updated_at']