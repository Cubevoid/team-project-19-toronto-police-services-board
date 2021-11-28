from rest_framework import viewsets
from .serializers import MeetingMinutesSerializer
from .serializers import MeetingSerializer
from .serializers import AgendaSerializer
from .serializers import AgendaItemSerializer
from .models import Minutes
from .models import Meeting
from .models import Agenda
from .models import AgendaItem
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.permissions import IsAdminUser
from django.db.models import Q

# Create your views here.

class MeetingView(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.filter(meeting_type = 'PUB')

class PrivateMeetingView(NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.filter(~Q(meeting_type = 'PUB'))


class MinuteView(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = MeetingMinutesSerializer
    queryset = Minutes.objects.all()


class AgendaView(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()


class AgendaItemView(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = AgendaItemSerializer
    queryset = AgendaItem.objects.all()
