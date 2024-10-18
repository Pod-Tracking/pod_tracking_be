from rest_framework import serializers
from ..models.game_player_model import GamePlayer

class GamePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePlayer
        fields = ['id', 'game', 'player', 'deck', 'is_winner', 'is_archenemy', 'kills', 'created_at', 'updated_at']
