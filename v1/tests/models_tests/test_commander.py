from django.test import TestCase
from django.utils.timezone import make_aware
from datetime import datetime
from v1.models.player_model import Player
from v1.models.deck_model import Deck
from v1.models.commander_model import Commander


class CommanderModelTest(TestCase):
    def setUp(self):
        self.player1 = Player.objects.create(
            name="Player 1",
            email="readyplayerone@gmail.com",
            password="password"
        )

        self.deck = Deck.objects.create(
            player=self.player1,
            name="Test Deck",
            tcg_type="magic_the_gathering",
            deck_type="commander"
        )

        created_time = make_aware(datetime(2024, 8, 13, 8, 22, 18, 976534))
        updated_time = make_aware(datetime(2024, 8, 13, 8, 22, 18, 976534))

        self.commander = Commander.objects.create(
            deck=self.deck,
            name="Tiamat",
            colors=["B", "G", "R", "U", "W"],
            photo="https://cards.scryfall.io/normal/front/6/d/6dd0b9b0-55f4-4ce7-a916-6f23687f3fe4.jpg?16277094787",
            created_at=created_time,
            updated_at=updated_time
        )

        self.expected_commander_response = {
            "id": self.commander.id,
            "deck": self.deck.id,
            "name": "Tiamat",
            "colors": "Black, Green, Red, Blue, White",
            "photo": "https://cards.scryfall.io/normal/front/6/d/6dd0b9b0-55f4-4ce7-a916-6f23687f3fe4.jpg?16277094787",
            "created_at": created_time.isoformat(),
            "updated_at": updated_time.isoformat()
        }

    def test_commander_model_fields(self):
        commander = Commander.objects.get(pk=self.commander.id)

        commander_dict = {
            "id": commander.id,
            "deck": commander.deck.id,
            "name": commander.name,
            "colors": commander.colors,
            "photo": commander.photo,
            "created_at": commander.created_at.isoformat(),
            "updated_at": commander.updated_at.isoformat()
        }

        self.assertEqual(commander.deck, self.deck)
        self.assertEqual(commander_dict, self.expected_commander_response)
