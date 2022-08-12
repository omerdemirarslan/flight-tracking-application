from rest_framework.routers import SimpleRouter

from flight_tracking.views import AirportViewSet, FlightViewSet

app_name = "api/v1"
simple_router = SimpleRouter()

simple_router.register("airports", AirportViewSet)
simple_router.register("flights", FlightViewSet)

urlpatterns = simple_router.urls
