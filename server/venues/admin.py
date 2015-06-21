from django.contrib import admin
from venues.models import Venue

# Register your models here.
class VenueSportInline(admin.TabularInline):
	model = Venue.sports.through

class VenueAdmin(admin.ModelAdmin):

	inlines = [
			VenueSportInline,
	]

	fieldsets = (
		('Details', {
				'fields': ('name', 'location', 'timings', 'contactno')
		}),
		('Time Added', {
            'classes': ('collapse',),
            'fields': ('venue_create_time', 'venue_update_time')
        }),
	)

	# The DateTime fields are uneditable so the following command is used to display them anyways
	readonly_fields = ('venue_create_time','venue_update_time')
	# The different fields to show the list of signed up entries
	list_display = ('name', 'location', 'venue_create_time', 'venue_update_time')
	# The criteria for setting up a search feature
	search_fields = ('name', 'location')
	
	class Meta:
		model = Venue

admin.site.register(Venue, VenueAdmin)