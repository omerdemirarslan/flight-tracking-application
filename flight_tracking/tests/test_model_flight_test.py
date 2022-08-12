from flight_tracking.models import Flight
from flight_tracking.tests.test_base_test import TestBaseCase


class TestFlightCase(TestBaseCase):
    def setUp(self) -> None:
        self.create_flight_records()

    def tearDown(self) -> None:
        self.delete_all_airport_records()
        self.delete_all_flight_records()

    def test_create_instance_controls(self):
        flight_instance = Flight.objects.first()

        self.assertTrue(flight_instance)
