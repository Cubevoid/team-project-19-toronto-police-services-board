from rest_framework import serializers
from .models import Minutes
from .models import Agenda
from .models import AgendaItem
from .models import Meeting

class MeetingMinutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minutes
        fields = ('id','meeting', 'notes')

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
        fields = ('id','title', 'date', 'recording_link', 'description', 'meeting_type')
