from rest_framework import serializers
from ..models.pod_model import Pod

class PodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pod
        fields = ['id', 'name', 'tcg_type', 'created_at', 'updated_at']