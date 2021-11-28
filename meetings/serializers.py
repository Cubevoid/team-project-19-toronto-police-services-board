from rest_framework import serializers
from .models import Minutes
from .models import Agenda
from .models import AgendaItem
from .models import Meeting

class MeetingMinutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minutes
        fields = '__all__'
class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields =  '__all__'

class AgendaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaItem
        fields =  '__all__'

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields =  '__all__'
