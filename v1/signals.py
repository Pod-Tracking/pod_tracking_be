from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models.game_model import Game
from .models.commander_model import Commander
from .models.pod_player_model import PodPlayer
from .models.game_player_model import GamePlayer


"""
Consider using django's builtin 'transactions' logic to 
ensure the automated game logic either succeeds altogether 
or fails altogether.
"""


# Update the colors a deck by inheriting the values from the commander
@receiver(post_save, sender=Commander)
def update_inherited_deck_attributes(sender, instance, created, **kwargs):
    deck = instance.deck
    if created or 'colors' in kwargs.get('update_fields', []):
        deck.colors = instance.colors
        deck.photo = instance.photo
        deck.save()

@receiver(pre_delete, sender=Commander)
def clear_inherited_deck_attributes(sender, instance, **kwargs):
    deck = instance.deck
    deck.colors = None
    deck.photo = None
    deck.save()


# Update the deck and pod_players stats after a game
@receiver(post_save, sender=GamePlayer)
def update_player_stats(sender, instance, created, **kwargs):
    pod_player = PodPlayer.objects.get(player=instance.player, pod=instance.game.pod)

    # Increment games, wins, kills, archenemy stats
    pod_player.total_games += 1
    pod_player.total_games += instance.kills
    
    if instance.is_winner:
        pod_player.total_wins += 1
    
    deck = instance.deck
    if instance.is_winner:
        deck.total_wins += 1
    deck.total_games += 1
    deck.save()

    if instance.is_archenemy:
        pod_player.games_as_archenemy += 1
        if instance.is_winner:
            pod_player.wins_as_archenemy += 1

    pod_player.save()

@receiver(post_save, sender=Game)
def update_game_stats(sender, instance, created, **kwargs):
    if created:
        GamePlayer.objects.filter(game=instance, deck=instance.winner).update(is_winner=True)

@receiver(pre_delete, sender=Game)
def handle_game_deletion(sender, instance, **kwargs):
    game_players = GamePlayer.objects.filter(game=instance)

    for game_player in game_players:
        player = game_player.player
        deck = game_player.deck
        pod_player = PodPlayer.objects.get(player=player, pod=instance.pod)

        if game_player.is_winner:
            player.total_wins -= 1
            pod_player.total_wins -= 1
            deck.total_wins -= 1

        player.total_games -= 1
        pod_player.total_games -= 1
        deck.total_games -= 1
        player.total_kills -= game_player.kills
        pod_player.total_kills -= game_player.kills

        player.save()
        pod_player.save()
        deck.save()

    game_players.delete()
