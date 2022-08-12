from rest_framework import serializers

from flight_tracking.models import Flight, Airport


class AirportSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField(required=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Airport
        fields = ["id", "code", "name"]


class AirportCodeField(serializers.RelatedField):
    def to_internal_value(self, code):
        airport = Airport.objects.filter(code=code).first()

        if not airport:
            raise serializers.ValidationError(f'No airport exists with code {code}')

        return airport

    def to_representation(self, value):
        return value.code


class FlightSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    flight_number = serializers.CharField(required=True)
    take_off = serializers.DateTimeField(required=True)
    landing = serializers.DateTimeField(required=True)
    to = AirportCodeField(source="destination", queryset=Airport.objects.none())

    class Meta:
        model = Flight
        fields = ["id", "flight_number", "take_off", "landing", "to", "from"]


FlightSerializer._declared_fields["from"] = AirportCodeField(
    source="location", queryset=Airport.objects.none()
)
