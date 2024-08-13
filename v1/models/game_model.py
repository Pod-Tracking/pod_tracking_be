from django.db import models
from ..models.pod_model import Pod
from ..models.deck_model import Deck

class Game(models.Model):
    pod = models.ForeignKey(Pod, on_delete=models.CASCADE)
    winner = models.ForeignKey(Deck, on_delete=models.SET_NULL, related_name='won_games', null=True)

    game_log = models.TextField(max_length=1000, null=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Game from {self.created_date}, in the '{self.pod.name}' Pod"
