from django.contrib import admin

from meetings.models import Agenda, AgendaItem, MeetingMinutes

# Register your models here.
admin.site.register(AgendaItem)
admin.site.register(Agenda)
admin.site.register(MeetingMinutes)