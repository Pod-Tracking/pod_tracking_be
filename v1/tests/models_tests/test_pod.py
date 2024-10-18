from django.test import TestCase
from django.db import IntegrityError
from rest_framework import serializers
from django.utils.timezone import make_aware
from datetime import datetime
from v1.utils import validate_tcg_type
from v1.serializers.pod_serializer import PodSerializer
from v1.models.player_model import Player
from v1.models.pod_model import Pod
# To run the test file, run the following line in the terminal:
# python3 manage.py test v1.tests.models_tests.test_pod


class PodModelTest(TestCase):
    def setUp(self):
        self.pod1 = Pod.objects.create(
            name="My First Pod",
            tcg_type=validate_tcg_type("MAGIC")
        )

        self.expected_pod_response = {
            "id": self.pod1.id,
            "name": "My First Pod",
            "tcg_type": "MAGIC",
        }


    # Happy path testing
    def test_pod_model_fields(self):
        pod = Pod.objects.get(pk=self.pod1.id)

        pod_dict = {
            "id": pod.id,
            "name": pod.name,
            "tcg_type": pod.tcg_type,
        }

        self.assertEqual(pod_dict["id"], self.expected_pod_response["id"])
        self.assertEqual(pod_dict["name"], self.expected_pod_response["name"])
        self.assertEqual(pod_dict["tcg_type"], self.expected_pod_response["tcg_type"])

    def test_create_pod_with_valid_data(self):
        pod = Pod.objects.create(
            name="New pod",
            tcg_type=validate_tcg_type("MAGIC"),
        )

        self.assertEqual(pod.name, "New pod")
        self.assertEqual(pod.tcg_type, "MAGIC")


    # Sad path testing
    def test_create_pod_with_invalid_tcg_type(self):
        with self.assertRaises(ValueError):
            Pod.objects.create(
                name="Invalid TCG pod",
                tcg_type=validate_tcg_type("invalid_tcg"),  # Invalid TCG type
            )

    def test_create_pod_without_name(self):
        with self.assertRaises(IntegrityError):
            Pod.objects.create(
                name=None, # Invalid name
                tcg_type=validate_tcg_type("MAGIC"),
            )
