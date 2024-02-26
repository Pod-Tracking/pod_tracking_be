from django.db import models
from ..models.player_model import Player

class Deck(models.Model):
    name = models.CharField(max_length=255)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=False)
    colors = models.CharField(max_length=100, default='')
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def __str__(self):
        return self.name