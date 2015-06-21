from rest_framework import serializers
from eventhandler.models import Team, League, Event, MiniEvent
from sports.serializers import SportSerializer
from venues.serializers import VenueSerializer

class TeamSerializer(serializers.ModelSerializer):
	sport = SportSerializer(read_only=True)

	class Meta:
		model = Team
		fields = ('name', 'manager', 'team_create_time', 'team_update_time', 'sport' )

class LeagueSerializer(serializers.ModelSerializer):
	sports = SportSerializer(many=True, read_only=True)
	teams = TeamSerializer(many=True, read_only=True)

	class Meta:
		model = League
		fields = ('name', 'manager', 'league_create_time', 'league_update_time', 'sports', 'teams' )

class EventSerializer(serializers.ModelSerializer):
	venue = VenueSerializer(read_only=True)
	league = LeagueSerializer(read_only=True)
	teams = TeamSerializer(many=True, read_only=True)

	class Meta:
		model = Event
		fields = ('name', 'manager', 'event_create_time', 'event_update_time', 'venue', 'league', 'teams' )

class MiniEventSerializer(serializers.ModelSerializer):
	event = EventSerializer(read_only=True)
	venue = VenueSerializer(read_only=True)
	league = LeagueSerializer(read_only=True)
	teams = TeamSerializer(many=True, read_only=True)

	class Meta:
		model = MiniEvent
		fields = ('name', 'manager', 'event_create_time', 'event_update_time', 'event', 'venue', 'league', 'teams' )