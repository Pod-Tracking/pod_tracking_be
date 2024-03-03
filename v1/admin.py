from django.contrib import admin
from .models.commander_model import Commander
from .models.player_model import Player
from .models.deck_model import Deck
from .models.pod_model import Pod
from .models.pod_player_model import PodPlayer
from .models.game_model import Game

admin.site.register(Player)
admin.site.register(Commander)
admin.site.register(Deck)
admin.site.register(Pod)
admin.site.register(Game)
admin.site.register(PodPlayer)

# Register your models here.
