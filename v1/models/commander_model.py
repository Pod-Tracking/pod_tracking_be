from django.db import models
from ..models.deck_model import Deck

class Commander(models.Model):
    deck = models.OneToOneField(Deck, on_delete=models.CASCADE, null=False, default=None)

    name = models.CharField(max_length=255)
    colors = models.CharField(max_length=255, blank=True, null=True)
    photo = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
