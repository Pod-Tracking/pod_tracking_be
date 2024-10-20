from django.db import models
from ..models.player_model import Player
from ..models.pod_model import Pod

class PodPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=False)
    pod = models.ForeignKey(Pod, on_delete=models.CASCADE, null=False)

    total_games = models.IntegerField(default=0)
    total_wins = models.IntegerField(default=0)
    games_as_archenemy = models.IntegerField(default=0)
    wins_as_archenemy = models.IntegerField(default=0)
    total_kills = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Player: {self.player.name} in the '{self.pod.name}' Pod"
