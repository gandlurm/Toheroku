from rest_framework import viewsets
from sports.models import Sport
from sports.serializers import SportSerializer

class SportViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Sport.objects.all()
	serializer_class = SportSerializer
