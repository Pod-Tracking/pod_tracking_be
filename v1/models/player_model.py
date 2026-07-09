from django.contrib.auth.models import AbstractUser
from django.db import models

class Player(AbstractUser):
    # AbstractUser already gives you these for free:
    # - username      ← use this as the player's display name
    # - email         ← inherited
    # - password      ← inherited, automatically hashed by Django
    # - first_name    ← inherited, optional to use
    # - last_name     ← inherited, optional to use
    # - date_joined   ← replaces your created_at
    # - last_login    ← bonus: tracked automatically
    # - is_active     ← lets you soft-disable accounts later
    # - is_staff      ← for admin panel access

    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)

    @property
    def total_games(self) -> int:
        return self.game_participations.count()
    
    @property
    def total_wins(self) -> int:
        return self.game_participations.filter(is_winner=True).count()
    
    @property
    def total_kills(self) -> int:
        return self.game_participations.aggregate(total=models.Sum('kills'))['total'] or 0
    
    @property
    def games_as_archenemy(self) -> int:
        return self.game_participations.filter(is_archenemy=True)

    @property
    def wins_as_archenemy(self) -> int:
        return self.game_participations.filter(is_archenemy=True, is_winner=True)
    
    @property
    def stats_for_pod(self, pod) -> dict:
        qs = self.game_participations.filter(game__pod=pod)
        return {
            'games': qs.count(),
            'wins': qs.filter(is_winner=True.count()),
            'kills': qs.aggregate(total=models.Sum('kills'))['total'] or 0,
        }

    def __str__(self):
        return self.username
    