from django.db import models
from ..models.pod_model import Pod
from ..models.deck_model import Deck
from ..models.pod_player_model import PodPlayer
from django.db.models.signals import m2m_changed

import pdb

class Game(models.Model):
    pod = models.ForeignKey(Pod, on_delete=models.CASCADE)
    winner = models.ForeignKey(Deck, on_delete=models.SET_NULL, related_name='won_games', null=True)
    decks = models.ManyToManyField(Deck, related_name='all_games')
    game_log = models.TextField(max_length=1000, null=False, default='')
    created_date = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         if self.pk is not None:
#             if self.winner:
#                 self.winner.wins += 1
#                 self.winner.save()

#     def __str__(self):
#         return f"Game from {self.created_date}, in the '{self.pod.name}' Pod"

#     def update_decks_games(self):
#         for deck in self.decks.all():
#             deck.total_games += 1

# # Signal to handle changes in the many-to-many relationship between Game and Deck
# def update_decks_games(sender, instance, action, **kwargs):
#     if action == 'post_add':
#         instance.update_decks_games()

# m2m_changed.connect(update_decks_games, sender=Game.decks.through)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_winner_wins()

    def update_winner_wins(self):
        if self.winner:
            self.winner.wins += 1
            self.winner.save()

    def update_decks_total_games(self):
        for deck in self.decks.all():
            deck.total_games += 1
            deck.save()

    def update_pod_players_stats(self):
        for deck in self.decks.all():
            pod_players = PodPlayer.objects.filter(pod=self.pod, player=deck.player)
            for pod_player in pod_players:
                pod_player.total_games += 1
                if deck == self.winner:
                    pod_player.total_wins += 1
                pod_player.save()

    def __str__(self):
        return f"Game from {self.created_date}, in the '{self.pod.name}' Pod"

# Signal to handle changes in the many-to-many relationship between Game and Deck
def update_decks_and_pod_players(sender, instance, action, **kwargs):
    if action == 'post_add':
        instance.update_decks_total_games()
        instance.update_pod_players_stats()

m2m_changed.connect(update_decks_and_pod_players, sender=Game.decks.through)