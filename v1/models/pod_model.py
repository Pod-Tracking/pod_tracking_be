from django.db import models
from django.utils import timezone
from models.player_model import Player
from ..enums.tcg_type_enum import TcgType

class Pod(models.Model):
    # add the 'admin' logic for when we start creating pods within the app
    # pod_admin = models.ForeignKey(Player, on_delete=models.CASCADE, null=False)

    name = models.CharField(max_length=50, null=False)
    pod_tcg = models.CharField(max_length=50, null=False, choices=TcgType.choices())

    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name