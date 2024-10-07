from django.test import TestCase
from django.utils.timezone import make_aware
from datetime import datetime
from v1.utils import process_colors
from v1.models.player_model import Player
from v1.models.deck_model import Deck
# To run the test file, run the following line in the terminal:
# python3 manage.py test v1.tests.models_tests.test_deck


class DeckModelTest(TestCase):
    def setUp(self):
        self.player1 = Player.objects.create(
            name="Player 1",
            email="readyplayerone@gmail.com",
            password="password"
        )

        self.player2 = Player.objects.create(
            name="Player 2",
            email="readyplayertwo@gmail.com",
            password="password"
        )

        self.deck1 = Deck.objects.create(
            player=self.player1,
            name="Test Deck",
            tcg_type="magic_the_gathering",
            deck_type="commander"
        )

        self.expected_deck_response = {
            "id": self.deck1.id,
            "name": "Test Deck",
            "tcg_type": "magic_the_gathering",
            "deck_type": "commander"
        }


    # Happy path testing
    def test_deck_model_fields(self):
        deck = Deck.objects.get(pk=self.deck1.id)

        deck_dict = {
            "id": deck.id,
            "name": deck.name,
            "tcg_type": deck.tcg_type,
            "deck_type": deck.deck_type
        }

        self.assertEqual(deck_dict["id"], self.expected_deck_response["id"])
        self.assertEqual(deck_dict["name"], self.expected_deck_response["name"])
        self.assertEqual(deck_dict["tcg_type"], self.expected_deck_response["tcg_type"])
        self.assertEqual(deck_dict["deck_type"], self.expected_deck_response["deck_type"])

    def test_create_deck_with_valid_data(self):
        deck = Deck.objects.create(
            player=self.player1,
            name="New Deck",
            tcg_type="magic_the_gathering",
            deck_type="standard"
        )

        self.assertEqual(deck.name, "New Deck")
        self.assertEqual(deck.tcg_type, "magic_the_gathering")
        self.assertEqual(deck.deck_type, "standard")
        self.assertEqual(deck.player, self.player1)

