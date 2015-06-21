from rest_framework import viewsets
from venues.models import Venue
from venues.serializers import VenueSerializer

class VenueViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Venue.objects.all()
	serializer_class = VenueSerializer