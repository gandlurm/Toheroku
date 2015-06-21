from django.contrib import admin
from eventhandler.models import Team, League, Event, MiniEvent

''' ManyToManyInlines'''

class LeagueSportInline(admin.TabularInline):
	model = League.sports.through

class LeagueTeamInline(admin.TabularInline):
	model = League.teams.through

class EventTeamInline(admin.TabularInline):
	model = Event.teams.through

class MiniEventTeamInline(admin.TabularInline):
	model = MiniEvent.teams.through

''' ForeignKeyInlines'''

class LeagueInline(admin.TabularInline):
	model = League

class TeamAdmin(admin.ModelAdmin):

	inlines = [
		EventTeamInline, 
		LeagueTeamInline, 
		# SportInline,
	]

	fieldsets = (
        ('Details', {
            'fields': ('name', 'manager', 'sport')
        }),
        ('Time Added', {
            'classes': ('collapse',),
            'fields': ('team_create_time', 'team_update_time')
        }),
	)
	# The DateTime fields are uneditable so the following command is used to display them anyways
	readonly_fields = ('team_create_time','team_update_time')
	# The different fields to show the list of signed up entries
	list_display = ('name', 'manager', 'sport', 'team_create_time', 'team_update_time')
	# The criteria for setting up a search feature
	search_fields = ('name', 'manager')
	
	class Meta:
		model = Team

class LeagueAdmin(admin.ModelAdmin):

	inlines = [
		LeagueSportInline,
		LeagueTeamInline,
		# LeagueInline,
	]

	fieldsets = (
        ('Details', {
            'fields': ('name', 'manager')
        }),
        ('Time Added', {
            'classes': ('collapse',),
            'fields': ('league_create_time', 'league_update_time')
        }),
	)
	# The DateTime fields are uneditable so the following command is used to display them anyways
	readonly_fields = ('league_create_time','league_update_time')
	# The different fields to show the list of signed up entries
	list_display = ('name', 'manager', 'league_create_time', 'league_update_time')
	# The criteria for setting up a search feature
	search_fields = ('name', 'manager')
	
	class Meta:
		model = League


class EventAdmin(admin.ModelAdmin):

	inlines = [
		# SportInline, 
		# LeagueInline, 
		EventTeamInline,
	]

	fieldsets = (
        ('Details', {
            'fields': ('name', 'manager', 'venue', 'leagues')
        }),
        ('Time Added', {
            'classes': ('collapse',),
            'fields': ('event_create_time', 'event_update_time')
        }),
	)
	# The DateTime fields are uneditable so the following command is used to display them anyways
	readonly_fields = ('event_create_time','event_update_time')
	# The different fields to show the list of signed up entries
	list_display = ('name', 'manager', 'event_create_time', 'event_update_time')
	# The criteria for setting up a search feature
	search_fields = ('name', 'manager')
	
	class Meta:
		model = Event


class MiniEventAdmin(admin.ModelAdmin):

	inlines = [
		# SportInline, 
		# LeagueInline, 
		MiniEventTeamInline,
	]

	fieldsets = (
        ('Details', {
            'fields': ('name', 'manager', 'venue', 'leagues', 'event')
        }),
        ('Time Added', {
            'classes': ('collapse',),
            'fields': ('minievent_create_time', 'minievent_update_time')
        }),
	)
	# The DateTime fields are uneditable so the following command is used to display them anyways
	readonly_fields = ('minievent_create_time','minievent_update_time')
	# The different fields to show the list of signed up entries
	list_display = ('name', 'manager', 'minievent_create_time', 'minievent_update_time')
	# The criteria for setting up a search feature
	search_fields = ('name', 'manager')
	
	class Meta:
		model = MiniEvent

admin.site.register(Team, TeamAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(MiniEvent, MiniEventAdmin)
