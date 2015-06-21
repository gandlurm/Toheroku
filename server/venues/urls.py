# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from venues.views import VenueViewSet

urlpatterns = patterns('',
                       url(r'^venue_details/$', VenueViewSet.as_view(), name='venue_details'))
