from django.contrib import admin

from meetings.models import *


class AgendaItemInline(admin.StackedInline):
    model = AgendaItem
    extra = 1


class AgendaAdmin(admin.ModelAdmin):
    inlines = [AgendaItemInline]


# Register your models here.
admin.site.register(Meeting)
admin.site.register(MeetingMinutes)
admin.site.register(Agenda, AgendaAdmin)
