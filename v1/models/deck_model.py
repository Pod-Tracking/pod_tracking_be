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
    archived = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_games(self) -> int:
        return self.game_participations.count()
    
    @property
    def total_wins(self) -> int:
        return self.game_participations.filter(is_winner=True).count()
    
    @property
    def current_commander(self):
        return self.commanders.filter(is_current=True).first()

    def __str__(self):
        return self.name
