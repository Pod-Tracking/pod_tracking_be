from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)

    total_games = models.IntegerField(default=0)
    total_wins = models.IntegerField(default=0)
    games_as_arch = models.IntegerField(default=0)
    wins_as_arch = models.IntegerField(default=0)
    total_kills = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    