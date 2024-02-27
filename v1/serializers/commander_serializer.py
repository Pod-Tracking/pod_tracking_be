from rest_framework import serializers
from ..models.commander_model import Commander
import pdb

class CommanderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commander
        fields = ['id', 'name', 'colors', 'img']