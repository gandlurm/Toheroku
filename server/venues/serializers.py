from rest_framework import serializers
from venues.models import Venue
from sports.serializers import SportSerializer

class VenueSerializer(serializers.ModelSerializer):
	sports = SportSerializer(many=True, read_only=True)

	class Meta:
		model = Venue
		fields = ('name', 'location', 'timings', 'contactno', 'venue_create_time', 'venue_update_time', 'sports')