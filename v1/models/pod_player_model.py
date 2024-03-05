from django.db import models
from ..models.player_model import Player
from ..models.pod_model import Pod

class PodPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=False)
    pod = models.ForeignKey(Pod, on_delete=models.CASCADE, null=False)
    total_wins = models.IntegerField(default=0)
    total_games = models.IntegerField(default=0)
    total_win_perc = models.FloatField(default=0)
    total_kills = models.IntegerField(default=0)
    kill_avg = models.FloatField(default=0)
    games_as_arch = models.IntegerField(default=0)
    wins_as_arch = models.IntegerField(default=0)

    def __str__(self):
        return f"Player: {self.player.name} in the '{self.pod.name}' Pod"
    
    def calc_win_perc(self):
        if self.total_games > 0:
            self.total_win_perc = (self.total_wins / self.total_games) * 100
        else:
            self.total_win_perc = 0.0
        self.save()

    def calc_kill_avg(self):
        if self.total_kills > 0:
            self.kill_avg = (self.total_kills / self.total_games) * 100
        else:
            self.total_kills = 0
        self.save()

    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         for deck in self.decks.all():
    #             deck.total_games += 1
    #             deck.save()
    #         if self.winner:
    #             self.winner.wins += 1
    #             self.winner.save()
    #         for deck in self.decks.exclude(pk=self.winner.pk):
    #             deck.update_win_percentage()
    #             # update PodPlayer
    
    # Next step is to automate the values of pod_player's wins, games, games_as_arch, etc, as game objects are logged...