from django.db import models
from ..models.deck_model import Deck
from ..models.player_model import Player
from ..models.game_model import Game

class GamePlayer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.SET_NULL, null=True)

    is_winner = models.BooleanField(default=False)
    is_archenemy = models.BooleanField(default=False)
    kills = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        formatted_game_date = self.game.created_at.strftime("%Y-%m-%d %H:%M")
        return f"'{self.player.name}' in {formatted_game_date} game playing the '{self.deck.name}' deck"
