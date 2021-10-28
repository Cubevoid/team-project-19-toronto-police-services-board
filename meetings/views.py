from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MeetingMinutesSerializer
from .models import Minutes

# Create your views here.
class MMView(viewsets.ModelViewSet):
    serializer_class = MeetingMinutesSerializer
    queryset = Minutes.objects.all()