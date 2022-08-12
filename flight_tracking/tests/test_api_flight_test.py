from datetime import datetime, timedelta

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from flight_tracking.tests.test_base_test import TestBaseCase
from flight_tracking.models import Airport, Flight


datetime_now = datetime.now()


class TestFlightAPICase(APITestCase, TestBaseCase):
    def setUp(self) -> None:
        self.create_flight_records()

    def tearDown(self) -> None:
        self.delete_all_airport_records()
        self.delete_all_flight_records()

    def test_flight_list_all_instance_controls(self):
        flight_all_instance = Flight.objects.all().count()

        url = reverse("api-v1:flight-list")
        response = self.client.get(url)
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result["results"]), flight_all_instance)

    def test_flight_get_instance_by_pk_controls(self):
        fight_first_instance = Flight.objects.first()

        url = reverse("api-v1:flight-detail", kwargs={"pk": fight_first_instance.id})
        response = self.client.get(url)
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(result["flight_number"], fight_first_instance.flight_number)
        self.assertEqual(result["to"], fight_first_instance.destination.code)

    def test_flight_create_instance_controls(self):
        airport_data_one, airport_data_two = Airport.objects.all()[:2]

        url = reverse("api-v1:flight-list")
        data = {
            "flight_number": "TK3561",
            "take_off": datetime_now,
            "landing": datetime_now + timedelta(days=1, hours=4),
            "to": airport_data_one.code,
            "from": airport_data_two.code,
        }
        response = self.client.post(url, data=data, format="json")
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result["flight_number"], "TK3561")

    def test_flight_update_instance_controls(self):
        flight_instance = Flight.objects.first()

        url = reverse("api-v1:flight-detail", kwargs={"pk": flight_instance.id})
        data = {
            "flight_number": "TK3565",
        }
        response = self.client.patch(url, data=data, format="json")
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["flight_number"], "TK3565")

    def test_flight_delete_instance_controls(self):
        flight_instance = Flight.objects.first()

        url = reverse("api-v1:flight-detail", kwargs={"pk": flight_instance.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_flight_get_total_record_controls(self):
        total_count = Flight.objects.filter(flight_number="TK3534").count()

        data = {
            "flight_number": "TK3534",
        }
        url = reverse("api-v1:flight-total-flights")
        response = self.client.get(url, data=data)
        result = response.json()[0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["count"], total_count)
