from django.contrib import admin
from sports.models import Sport

class SportAdmin(admin.ModelAdmin):
    # The fields to display and the categories they need to be put into:
	fieldsets = (
        ('Details', {
            'fields': ('name',),
        }),
	)
	list_display = ('name',)
	# The criteria for setting up a search feature
	search_fields = ('name',)
	
	class Meta:
		model = Sport

admin.site.register(Sport, SportAdmin)
