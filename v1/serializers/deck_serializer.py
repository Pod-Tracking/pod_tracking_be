from rest_framework import serializers
from ..models.deck_model import Deck

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'player', 'cmdr', 'name', 'tcg', 'deck_type', 'colors', 'photo', 'total_wins', 'total_losses', 'created_date', 'updated_date']