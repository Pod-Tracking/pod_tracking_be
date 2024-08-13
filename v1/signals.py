from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.commander_model import Commander

@receiver(post_save, sender=Commander)
# If a new commander is created, update the colors of the related deck
def update_deck_colors(sender, instance, created, **kwargs):
    if created:
        deck = instance.deck
        deck.colors = instance.colors
        deck.photo = instance.photo
        deck.save()