from django.core.exceptions import ValidationError
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

    def clean(self):
        # Check if total_turns is a positive and an integer
        if self.total_turns is not None:
            if not isinstance(self.total_turns, int):
                raise ValidationError("The total_turns value must be an integer.")
            if self.total_turns < 0:
                raise ValidationError("The total_turns value must be a positive number.")
