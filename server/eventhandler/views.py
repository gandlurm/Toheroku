# from rest_framework import generics
from rest_framework import viewsets
from eventhandler.models import Team, League, Event, MiniEvent
from eventhandler.serializers import TeamSerializer, LeagueSerializer, EventSerializer, MiniEventSerializer

# from django.http import HttpResponse
# from django.shortcuts import render
# from rest_framework.response import Response

# # Create your views here.
class TeamViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class LeagueViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = League.objects.all()
	serializer_class = LeagueSerializer

class EventViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer

class MiniEventViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = MiniEvent.objects.all()
	serializer_class = MiniEventSerializer

# class SportsCentreList(generics.ListCreateAPIView):
#     """List all addresses or create a new Address"""
#     queryset = Venue.objects.all()
#     model = Venue
#     serializer_class = VenueSerializer
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = VenueSerializer(queryset, many=True)
#         return Response(serializer.data)
    
# class SportsCentreDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, update or delete an instance.
#     """
#     model = Venue
#     serializer_class = VenueSerializer

# def SportsCentreView(request):
#     if request.method == 'POST':
#         form = VenueForm(request.POST)
#         name = request.POST.get('name','')
#         location = request.POST.get('location', '')
#         timings = request.POST.get('timings', '')
#         sports = request.POST.get('sports', '')
#         contactno = request.POST.get('contactno', '')
#         finObject = Venue(name = name, location = location, timings = timings, sports = sports, contactno = contactno)
#         finObject.save()
#         return HttpResponseRedirect(reverse('SportReg:registration'))

#     else:
#         form = VenueForm()
#         return render (request, 'SportReg/registration.html', {
#             'form': form,
#     })
            
# class TeamDashboardView(generics.ListCreateAPIView):
#     """List all addresses or create a new Address"""
#     queryset = Venue.objects.all()
#     model = Venue
#     serializer_class = VenueSerializer
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = VenueSerializer(queryset, many=True)
#         return Response(serializer.data)
    

            
