from django.contrib import admin
from .models.commander_model import Commander
from .models.player_model import Player
from .models.deck_model import Deck

admin.site.register(Player)
admin.site.register(Commander)
admin.site.register(Deck)

# Register your models here.
