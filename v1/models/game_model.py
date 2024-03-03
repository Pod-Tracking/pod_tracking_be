from django.db import models
from ..models.pod_model import Pod
from ..models.deck_model import Deck

class Game(models.Model):
    pod = models.ForeignKey(Pod, on_delete=models.CASCADE)
    decks = models.ManyToManyField(Deck)
    winner = models.ForeignKey(Deck, on_delete=models.SET_NULL, related_name='won_games', null=True)
    losers = models.ManyToManyField(Deck, related_name='lost_games')
    game_log = models.TextField(max_length=1000, null=True, default='')
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.pk is not None:
            for deck in self.decks.all():
                deck.total_games += 1
                deck.save()
            if self.winner:
                self.winner.wins += 1
                self.winner.save()

    def __str__(self):
        return f"Game from {self.created_date}, in the '{self.pod.name}' Pod"