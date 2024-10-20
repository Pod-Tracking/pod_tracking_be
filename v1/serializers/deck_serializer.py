from rest_framework import serializers
from ..models.deck_model import Deck
import pdb

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'player', 'name', 'tcg_type', 'deck_type', 'colors', 'photo', 'total_wins', 'total_games', 'created_at', 'updated_at']

    def validate(self, data):
        if not data.get('player'):
            raise serializers.ValidationError("The deck player is required.")
        
        if not data.get('name') or len(data.get('name') == 0):
            raise serializers.ValidationError("The deck name is required.")
        
        if not data.get('tcg_type'):
            raise serializers.ValidationError("The deck tcg_type is required.")

        if not data.get('deck_type'):
            raise serializers.ValidationError("The deck deck_type is required.")        

        return data
