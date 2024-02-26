from rest_framework import serializers
from ..models.deck_model import Deck
# from ..models.player_model import Player
# from ..models.commander_model import Commander

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ['name', 'player', 'colors', 'wins', 'losses']