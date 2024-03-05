from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    total_wins = models.IntegerField(default=0)
    total_games = models.IntegerField(default=0)
    total_win_perc = models.FloatField(default=0)
    total_kills = models.IntegerField(default=0)
    kill_avg = models.FloatField(default=0)
    games_as_arch = models.IntegerField(default=0)
    wins_as_arch = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
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
