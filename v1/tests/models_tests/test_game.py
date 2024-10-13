from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.utils.timezone import make_aware
from datetime import datetime
from v1.utils import validate_tcg_type
from v1.serializers.game_serializer import GameSerializer
from v1.models.pod_model import Pod
from v1.models.game_model import Game
# To run the test file, run the following line in the terminal:
# python3 manage.py test v1.tests.models_tests.test_game


class GameModelTest(TestCase):
    def setUp(self):
        self.pod1 = Pod.objects.create(
            name="Pod 1",
            tcg_type=validate_tcg_type("MAGIC")
        )

        self.pod2 = Pod.objects.create(
            name="Pod 2",
            tcg_type=validate_tcg_type("MAGIC")
        )

        self.game1 = Game.objects.create(
            pod=self.pod1,
            total_turns=10,
            game_log="So-and-so won the game by utilizing the heart of the cards."
        )

        self.expected_game_response = {
            "id": self.game1.id,
            "pod": self.pod1.id,
            "total_turns": 10,
            "game_log": "So-and-so won the game by utilizing the heart of the cards."
        }


    # Happy path testing
    def test_game_model_fields(self):
        game = Game.objects.get(pk=self.game1.id)

        game_dict = {
            "id": game.id,
            "pod": game.pod.id,
            "total_turns": game.total_turns,
            "game_log": game.game_log
        }

        self.assertEqual(game_dict["id"], self.expected_game_response["id"])
        self.assertEqual(game_dict["pod"], self.expected_game_response["pod"])
        self.assertEqual(game_dict["total_turns"], self.expected_game_response["total_turns"])
        self.assertEqual(game_dict["game_log"], self.expected_game_response["game_log"])

    def test_create_game_with_valid_data(self):
        game2 = Game.objects.create(
            pod=self.pod2,
            total_turns=5,
            game_log="I won the game.",
        )
        game2.full_clean()
        game2.save()

        self.assertEqual(game2.id, 2)
        self.assertEqual(game2.pod, self.pod2)
        self.assertEqual(game2.total_turns, 5)
        self.assertEqual(game2.game_log, "I won the game.")


    # Sad path testing
    def test_create_game_with_invalid_pod(self):
        with self.assertRaises(IntegrityError):
            Game.objects.create(
                pod=None, # Invalid pod reference
                total_turns=10,
                game_log="Invalid pod id"
            )


    def test_create_game_with_negative_total_turns(self):
        game = Game(
            pod=self.pod1,
            total_turns=-5,  # Invalid negative number
            game_log="Invalid game log"
        )
        with self.assertRaises(ValidationError) as e:
            game.full_clean()  # This triggers the clean() method

        self.assertIn('__all__', e.exception.message_dict)
        self.assertEqual(e.exception.message_dict['__all__'], ['The total_turns value must be a positive number.'])


    def test_create_game_with_invalid_total_turns_value(self):
        game = Game(
            pod=self.pod1,
            total_turns="invalid",  # Invalid data type
            game_log="Invalid data type for total_turns"
        )
        with self.assertRaises(ValidationError) as e:
            game.full_clean()

        self.assertIn('total_turns', e.exception.message_dict)        
        self.assertEqual(e.exception.message_dict['total_turns'], ['“invalid” value must be an integer.'])
