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

# Helper method
def update_stats(instance, stat_object: object, operation: str, is_deck=True):
    if operation == "add":
        modifier = 1
    elif operation == "subtract":
        modifier = -1

    stat_object.total_games += modifier
    if instance.is_winner:
        stat_object.total_wins += modifier

    if not is_deck:
        stat_object.total_kills += instance.kills
        if instance.is_archenemy:
            stat_object.games_as_archenemy += modifier
            if instance.is_winner:
                stat_object.wins_as_archenemy += modifier
    
    stat_object.save()


# Update the colors a deck by inheriting the values from the commander
@receiver(post_save, sender=Commander)
def update_inherited_deck_attributes(sender, instance, created, **kwargs):
    deck = instance.deck
    if created:
        deck.colors = instance.colors
        deck.photo = instance.photo
        deck.save()

@receiver(pre_delete, sender=Commander)
def clear_inherited_deck_attributes(sender, instance, **kwargs):
    deck = instance.deck
    deck.colors = None
    deck.photo = None
    deck.save()


# Update the Player, Deck, and PodPlayers stats after a GamePlayer is added
@receiver(post_save, sender=GamePlayer)
def update_player_stats(sender, instance, **kwargs):
    pod_player = PodPlayer.objects.get(player=instance.player, pod=instance.game.pod)
    deck = instance.deck
    player = instance.player

    update_stats(instance, pod_player, "add", is_deck=False)
    update_stats(instance, deck, "add")
    update_stats(instance, player, "add", is_deck=False)

# Updates the stats of a Player, Deck, and PodPlayer after a Game is deleted
@receiver(pre_delete, sender=Game)
def handle_game_deletion(sender, instance, **kwargs):
    game_players = GamePlayer.objects.filter(game=instance)

    for game_player in game_players:
        player = game_player.player
        deck = game_player.deck
        pod_player = PodPlayer.objects.get(player=player, pod=instance.pod)

        update_stats(game_player, pod_player, "subtract", is_deck=False)
        update_stats(game_player, deck, "subtract")
        update_stats(game_player, player, "subtract", is_deck=False)

    game_players.delete()
