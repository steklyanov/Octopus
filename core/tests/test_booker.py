from .common_test import create_user, login_user
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Booker
from rest_framework import status


class BookerTest(TestCase):
    """ Test for booker """
    def setUp(self) -> None:
        self.user = create_user(username="max", email="user@example.com")
        self.client = APIClient()
        login_user(self.client, self.user)

    def test_booker_can_get_own_details(self):
        booker = Booker()
        booker.user = self.user
        booker.save()
        response = self.client.get(reverse("octopus:booker_profile"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
