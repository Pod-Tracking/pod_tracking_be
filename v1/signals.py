from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.commander_model import Commander
from .models.deck_model import Deck

@receiver(post_save, sender=Commander)
def update_deck_colors(sender, instance, created, **kwargs):
    if created:
        # If a new commander is created, update the colors of the related deck
        deck = instance.deck
        deck.colors = instance.colors
        deck.save()