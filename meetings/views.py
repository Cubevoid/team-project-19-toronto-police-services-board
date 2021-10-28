from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MeetingMinutesSerializer
from .serializers import MeetingSerializer
from .serializers import AgendaSerializer
from .models import MeetingMinutes
from .models import Meeting
from .models import Agenda

# Create your views here.
class MMView(viewsets.ModelViewSet):
    serializer_class = MeetingMinutesSerializer
    queryset = MeetingMinutes.objects.all()

class AView(viewsets.ModelViewSet):
    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()

class MView(viewsets.ModelViewSet):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()
