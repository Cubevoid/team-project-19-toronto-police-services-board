from rest_framework import serializers
from .models import MeetingMinutes

class MeetingMinutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingMinutes
        fields = ('id','meeting', 'yt_link', 'notes')