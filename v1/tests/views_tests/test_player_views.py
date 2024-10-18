from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from v1.models.player_model import Player


class PlayerTestCase(APITestCase):
    def setUp(self):
        self.player1 = Player.objects.create(
            name="Player 1",
            email="readyplayer1@gmail.com",
            password="password"
        )

        self.player2 = Player.objects.create(
            name="Player 2",
            email="readyplayer2@gmail.com",
            password="password"
        )

    def test_get_player_list(self):
        url = reverse("v1_get_player_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], self.player1.id)
        self.assertEqual(response.data[0]["email"], self.player1.email)
        self.assertEqual(response.data[0]["password"], self.player1.password)

        self.assertEqual(response.data[1]["id"], self.player2.id)
        self.assertEqual(response.data[1]["email"], self.player2.email)
        self.assertEqual(response.data[1]["password"], self.player2.password)

    def test_post_player(self):
        url = reverse("v1_get_player_list")
        new_player_data = {
            "name": "player 3",
            "email": "readyplayer3@gmail.com",
            "password": "password"
        }
        response = self.client.post(url, new_player_data)

        self.assertEqual(response.status_code,status.HTTP_201_CREATED )
        self.assertEqual(Player.objects.count(), 3)
        self.assertEqual(response.data["id"], 3)
