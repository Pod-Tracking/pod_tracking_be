from django.db import models
from ..models.deck_model import Deck

class Commander(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, null=False, default=None, related_name='commanders')

    name = models.CharField(max_length=255)
    colors = models.CharField(max_length=255, blank=True, null=True)
    photo = models.URLField()
    is_current = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.is_current:
            Commander.objects.filter(deck=self.deck, is_current=True).exclude(pk=self.pk).update(is_current=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
