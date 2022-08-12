from flight_tracking.models import Airport
from flight_tracking.tests.test_base_test import TestBaseCase


class TestAirportCase(TestBaseCase):
    def setUp(self) -> None:
        self.create_airport_records()

    def tearDown(self) -> None:
        self.delete_all_airport_records()

    def test_airport_create_instance_controls(self):
        airport_instance = Airport.objects.first()

        self.assertTrue(airport_instance)
