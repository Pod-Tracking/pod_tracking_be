from django.db import models
from ..models.player_model import Player
from ..models.pod_model import Pod

class PodPlayer(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, null=False)
    pod = models.OneToOneField(Pod, on_delete=models.CASCADE, null=False)
    total_win_perc = models.FloatField()
    total_wins = models.IntegerField(default=0)
    total_games = models.IntegerField(default=0)
    total_kills = models.IntegerField(default=0)
    kil_avg = models.IntegerField(default=0)
    games_as_arch = models.IntegerField(default=0)
    wins_as_arch = models.IntegerField(default=0)

    def __str__(self):
        return f"Player: {self.player.name} in the '{self.pod.name}' Pod"