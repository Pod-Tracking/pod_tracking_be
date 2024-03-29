from rest_framework import serializers
from ..models.player_model import Player
import pdb

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['name', 'photo', 'email', 'password']