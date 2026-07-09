from django.db import models
from ..models.player_model import Player
from ..models.pod_model import Pod

class PodPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=False)
    pod = models.ForeignKey(Pod, on_delete=models.CASCADE, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('player', 'pod')

    def __str__(self):
        return f"Player: {self.player.username} in the '{self.pod.name}' Pod"
