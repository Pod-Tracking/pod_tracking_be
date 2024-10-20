from django.db import models
from ..models.player_model import Player
from ..enums.deck_type_enum import DeckType
from ..enums.tcg_type_enum import TcgType

class Deck(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=False)

    name = models.CharField(max_length=255, null=False)
    tcg_type = models.CharField(max_length=50, null=False, choices=TcgType.choices())
    deck_type = models.CharField(max_length=50, null=True, choices=DeckType.choices())
    colors = models.CharField(max_length=255, blank=True, null=True)
    photo = models.URLField(null=True, blank=True)
    total_games = models.IntegerField(default=0)
    total_wins = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
