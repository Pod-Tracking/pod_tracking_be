from rest_framework import serializers
from ..models.commander_model import Commander

class CommanderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commander
        fields = ['id', 'deck', 'name', 'colors', 'photo', 'created_at', 'updated_at']