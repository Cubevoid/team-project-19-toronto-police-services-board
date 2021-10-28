from rest_framework import serializers
from .models import MeetingMinutes
from .models import Agenda
from .models import Meeting

class MeetingMinutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingMinutes
        fields = ('id','meeting', 'yt_link', 'notes')

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id', 'meeting')

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id','title', 'date', 'description', 'meeting_type')
