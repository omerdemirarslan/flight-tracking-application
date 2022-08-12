from django.db.models import Count

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiParameter

from flight_tracking.serializers import AirportSerializer, FlightSerializer
from flight_tracking.models import Airport, Flight


class AirportViewSet(viewsets.ModelViewSet):
    serializer_class = AirportSerializer
    queryset = Airport.objects.all()


class FlightViewSet(viewsets.ModelViewSet):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()

    @extend_schema(
        description="Return total flight counts based on flight number.",
        methods=["GET"],
        parameters=[
            OpenApiParameter(name="flight_number", description="Filter by flight number", required=True, type=str)
        ],
    )
    @action(detail=False, methods=["GET"], url_name="total-flights")
    def total_flights(self, request):
        """
        This Method Returns Total Flight Count By flight_number
        :param request:
        :return:
        """
        flight_number = request.GET.get("flight_number")
        flights = Flight.objects.filter(flight_number=flight_number).values("flight_number").annotate(count=Count("id"))

        return Response(status=status.HTTP_200_OK, data=flights)
