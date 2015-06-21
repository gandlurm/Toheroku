# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers

from eventhandler.views import TeamViewSet, LeagueViewSet, EventViewSet, MiniEventViewSet
from sports.views import SportViewSet
from venues.views import VenueViewSet

router = routers.DefaultRouter()
router.register(r'sports', SportViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'leagues', LeagueViewSet)
router.register(r'events', EventViewSet)
router.register(r'minievents', MiniEventViewSet)


urlpatterns = patterns('api.views',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)