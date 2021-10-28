from rest_framework import serializers
from .models import MeetingMinutes
from .models import Agenda
from .models import AgendaItem
from .models import Meeting

class MeetingMinutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingMinutes
        fields = ('id','meeting', 'yt_link', 'notes')

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id', 'meeting')

class AgendaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaItem
        fields = ('id', 'agenda', 'title', 'description', 'result', 'motion', 'file')

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id','title', 'date', 'description', 'meeting_type')
