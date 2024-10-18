from django.test import TestCase
from django.utils.timezone import make_aware
from datetime import datetime
from v1.utils import process_colors
from v1.models.player_model import Player
from v1.models.deck_model import Deck
from v1.models.commander_model import Commander
from django.db import IntegrityError
# To run the test file, run the following line in the terminal:
# python3 manage.py test v1.tests.models_tests.test_commander


class CommanderModelTest(TestCase):
    def setUp(self):
        self.player1 = Player.objects.create(
            name="Player 1",
            email="readyplayerone@gmail.com",
            password="password"
        )

        self.deck1 = Deck.objects.create(
            player=self.player1,
            name="Test Deck",
            tcg_type="magic_the_gathering",
            deck_type="commander"
        )

        self.deck2 = Deck.objects.create(
            player=self.player1,
            name="Test Deck",
            tcg_type="magic_the_gathering",
            deck_type="commander"
        )

        self.commander = Commander.objects.create(
            deck=self.deck1,
            name="Tiamat",
            colors=process_colors(["B", "G", "R", "U", "W"]),
            photo="https://cards.scryfall.io/normal/front/6/d/6dd0b9b0-55f4-4ce7-a916-6f23687f3fe4.jpg?16277094787"
        )

        self.expected_commander_response = {
            "id": self.commander.id,
            "deck": self.deck1.id,
            "name": "Tiamat",
            "colors": "Black, Green, Red, Blue, White",
            "photo": "https://cards.scryfall.io/normal/front/6/d/6dd0b9b0-55f4-4ce7-a916-6f23687f3fe4.jpg?16277094787"
        }


    # Happy Path Testing
    def test_commander_model_fields(self):
        commander = Commander.objects.get(pk=self.commander.id)

        commander_dict = {
            "id": commander.id,
            "deck": commander.deck.id,
            "name": commander.name,
            "colors": commander.colors,
            "photo": commander.photo
        }

        self.assertEqual(commander_dict["id"], self.expected_commander_response["id"])
        self.assertEqual(commander_dict["deck"], self.expected_commander_response["deck"])
        self.assertEqual(commander_dict["name"], self.expected_commander_response["name"])
        self.assertEqual(commander_dict["colors"], self.expected_commander_response["colors"])
        self.assertEqual(commander_dict["photo"], self.expected_commander_response["photo"])

    def test_create_commander_with_valid_data(self):
        commander = Commander.objects.create(
            deck=self.deck2,
            name="Atraxa",
            colors=process_colors(["B", "G", "R", "W"]),
            photo="https://cards.scryfall.io/normal/front/a/t/atraxa.jpg"
        )
        self.assertIsInstance(commander, Commander)
        self.assertEqual(commander.name, "Atraxa")
        self.assertEqual(commander.colors, "Black, Green, Red, White")


    # Sad Path Testing
    def test_commander_requires_name(self):
        with self.assertRaises(ValueError):
            Commander.objects.create(
                deck=self.deck2,
                name=None,  # Invalid: No name provided
                colors=process_colors(["B", "G"]),
                photo="https://cards.scryfall.io/normal/front/n/a/nameless.jpg"
            )

    def test_invalid_deck_assignment(self):
        with self.assertRaises(IntegrityError):
            Commander.objects.create(
                deck_id=999,  # Invalid deck ID
                name="Invalid Deck Commander",
                colors=process_colors(["B", "U"]),
                photo="https://cards.scryfall.io/normal/front/i/n/invalid.jpg"
            )

    def test_invalid_color_value(self):
        with self.assertRaises(ValueError):
            Commander.objects.create(
                deck=self.deck2,
                name="Color Error Commander",
                colors=process_colors(["X", "Y"]),  # Invalid color values
                photo="https://cards.scryfall.io/normal/front/c/e/color-error.jpg"
            )
