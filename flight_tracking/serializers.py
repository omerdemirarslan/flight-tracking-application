from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
    RelatedField,
    ValidationError,
    DateTimeField,
)

from flight_tracking.models import Flight, Airport


class AirportSerializer(ModelSerializer):
    id = IntegerField(read_only=True)
    code = CharField(required=True)
    name = CharField(required=True)

    class Meta:
        model = Airport
        fields = ["id", "code", "name"]


class AirportCodeField(RelatedField):
    def to_internal_value(self, code: str) -> object:
        """
        This Method Controls Is There Airport By Code
        :param code:
        :return: Airport First Object or Raise ValidationError Message
        """
        airport_instance = Airport.objects.filter(code=code).first()

        if not airport_instance:
            message = "There is no airport exist code by %s"

            raise ValidationError(message % code.__name__)

        return airport_instance

    def to_representation(self, value) -> object:
        """
        This Method Returns Code Value
        :param value:
        :return:
        """
        return value.code


class FlightSerializer(ModelSerializer):
    id = IntegerField(read_only=True)
    flight_number = CharField(required=True)
    take_off = DateTimeField(required=True)
    landing = DateTimeField(required=True)
    to = AirportCodeField(source="destination", queryset=Airport.objects.none())

    class Meta:
        model = Flight
        fields = ["id", "flight_number", "take_off", "landing", "to", "from"]


FlightSerializer._declared_fields["from"] = AirportCodeField(source="location", queryset=Airport.objects.none())
