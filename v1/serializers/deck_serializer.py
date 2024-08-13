from rest_framework import serializers
from ..models.deck_model import Deck

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'player', 'name', 'tcg_type', 'deck_type', 'colors', 'photo', 'total_wins', 'total_games', 'created_at', 'updated_at']