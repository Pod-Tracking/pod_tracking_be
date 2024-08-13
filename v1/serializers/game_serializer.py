from rest_framework import serializers
from ..models.game_model import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'pod', 'winner', 'game_log', 'created_at', 'updated_at']
