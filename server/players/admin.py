from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    # The fields to display and the categories they need to be put into:
	fieldsets = (
        ('Details', {
            'fields': ('nick_name','user',),
        }),
	)
	list_display = ('nick_name',)
	# The criteria for setting up a search feature
	search_fields = ('nick_name',)
	
	class Meta:
		model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)