from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from flight_tracking.tests.test_base_test import TestBaseCase
from flight_tracking.models import Airport


class TestAirportAPICase(APITestCase, TestBaseCase):
    def setUp(self) -> None:
        self.create_airport_records()

    def tearDown(self) -> None:
        self.delete_all_airport_records()

    def test_airport_list_all_instance_controls(self):
        airport_all_instance = Airport.objects.all().count()

        url = reverse("api-v1:airport-list")
        response = self.client.get(url)
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(result["results"]), airport_all_instance)

    def test_airport_get_instance_by_pk_controls(self):
        airport_first_instance = Airport.objects.first()

        url = reverse("api-v1:airport-detail", kwargs={"pk": airport_first_instance.id})
        response = self.client.get(url)
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(result["code"], airport_first_instance.code)
        self.assertEqual(result["name"], airport_first_instance.name)

    def test_airport_create_instance_controls(self):
        url = reverse("api-v1:airport-list")
        data = {"code": "SCH", "name": "Samsun Carsamba Airport"}
        response = self.client.post(url, data=data, format="json")
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result["name"], "Samsun Carsamba Airport")

    def test_airport_update_instance_controls(self):
        airport_first_instance = Airport.objects.first()

        url = reverse("api-v1:airport-detail", kwargs={"pk": airport_first_instance.id})
        data = {
            "code": "TYZ",
        }
        response = self.client.patch(url, data=data, format="json")
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["code"], "TYZ")

    def test_airport_delete_instance_controls(self):
        airport_instance = Airport.objects.first()

        url = reverse("api-v1:airport-detail", kwargs={"pk": airport_instance.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
