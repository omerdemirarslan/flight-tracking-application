import unittest

from flight_tracking.models import Airport, Flight
from flight_tracking.tests.test_model_configs_test import *


class TestBaseCase(unittest.TestCase):
    @staticmethod
    def create_airport_records():
        for airport in airport_data_records:
            Airport.objects.create(**airport)

    def create_flight_records(self):
        self.create_airport_records()

        airport_data_one, airport_data_two = Airport.objects.all()[:2]

        for flight in flight_data_records:
            Flight.objects.create(
                **flight,
                destination=airport_data_one,
                location=airport_data_two,
            )

    @staticmethod
    def delete_all_airport_records():
        Airport.objects.all().delete()

    @staticmethod
    def delete_all_flight_records():
        Flight.objects.all().delete()


if __name__ == "__main__":
    unittest.main()
