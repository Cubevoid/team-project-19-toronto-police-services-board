from rest_framework import serializers
from .models import Minutes

class MeetingMinutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minutes
        fields = ('id','meeting', 'yt_link', 'notes')