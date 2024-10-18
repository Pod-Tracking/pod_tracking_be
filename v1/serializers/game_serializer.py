from rest_framework import serializers
from ..models.game_model import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'pod', 'total_turns', 'game_log', 'created_at', 'updated_at']

    def validate(self, data):
        if not data.get('pod'):
            raise serializers.ValidationError("The pod value is required.")

        total_turns = data.get('total_turns')
        if total_turns is not None:
            if not isinstance(total_turns, int):
                raise serializers.ValidationError("The data type for total_turns must be an integer.")

            if total_turns < 0:
                raise serializers.ValidationError("The value for total_turns must be a positive number.")

        return data
