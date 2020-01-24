from .common_test import create_user, login_user, create_booker, create_agency_booker_model
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


class BookerTest(TestCase):
    """ Test for booker """
    def setUp(self) -> None:
        self.user = create_user(username="max", email="user@example.com")
        self.client = APIClient()
        login_user(self.client, self.user)

    def test_booker_can_get_own_details(self):
        booker = create_booker(self.user)
        response = self.client.get(reverse("octopus:booker_profile"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booker_model_list(self):
        """ Test that booker see only own agency models"""
        booker, actor, agency = create_agency_booker_model(user=self.user)
        booker2, actor2, user2 = create_agency_booker_model(user=create_user())
        response = self.client.get(reverse("octopus:booker_list"))
        self.assertEqual(len(response.data), 1)
