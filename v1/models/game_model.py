from django.db import models
from ..models.pod_model import Pod

class Game(models.Model):
    pod = models.ForeignKey(Pod, on_delete=models.CASCADE)

    total_turns = models.IntegerField(default=None, null=True)
    game_log = models.TextField(max_length=1000, null=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        formatted_date = self.created_at.strftime("%Y-%m-%d %H:%M")
        return f"Game from {formatted_date}, in the '{self.pod.name}' Pod"
