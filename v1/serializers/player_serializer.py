from rest_framework import serializers
from ..models.player_model import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'photo', 'email', 'password', 'created_at', 'updated_at']