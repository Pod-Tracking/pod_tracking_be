from django.db import models
from ..models.player_model import Player
from django.utils import timezone

class Deck(models.Model):
    name = models.CharField(max_length=255, null=False)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=False)
    colors = models.CharField(max_length=100, default='')
    wins = models.IntegerField(default=0)
    total_games = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name