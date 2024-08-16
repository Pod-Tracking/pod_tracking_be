"""
URL configuration for market_nextdoor_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf import settings
from .views import player_views, deck_views, commander_views, pod_views, pod_player_views, game_views, game_player_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Player endpoints
    path('players', player_views.player_list),
    path('players/<int:player_id>', player_views.player_details),
    # Deck endpoints
    path('players/<int:player_id>/decks', deck_views.deck_list),
    path('players/<int:player_id>/decks/<int:deck_id>', deck_views.deck_details),
    # MTG Commander endpoints
    path('players/<int:player_id>/decks/<int:deck_id>/create_commander', commander_views.commander_list),
    path('players/<int:player_id>/decks/<int:deck_id>/deck_commander/<int:commander_id>', commander_views.commander_details),
    # Pod endpoints
    path('pods', pod_views.pod_list),
    path('pods/<int:pod_id>', pod_views.pod_details),
    # Pods by Player IDs endpoints
    path('players/<int:player_id>/pods', pod_player_views.pods_by_player_list),
    path('players/<int:player_id>/pods/<int:pod_id>', pod_player_views.pod_by_player_details),
    # Players by Pod IDs endpoints
    path('pods/<int:pod_id>/players', pod_player_views.players_by_pod),
    path('pods/<int:pod_id>/players/<int:player_id>', pod_player_views.players_by_pod),
    # Games endpoints
    path('pods/<int:pod_id>/games', game_views.game_list),
    path('pods/<int:pod_id>/games/<int:game_id>', game_views.game_details),
    # GamePlayer endpoints
    path('pods/<int:pod_id>/games/<int:game_id>/game_players', game_player_views.game_player_list),
    path('pods/<int:pod_id>/games/<int:game_id>/game_players/<int:game_player_id>', game_player_views.game_player_details),
]

