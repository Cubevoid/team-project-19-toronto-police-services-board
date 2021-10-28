from datetime import datetime
from django.db import models
import os
from pytz import timezone
from tpsb.settings import TIME_ZONE
from ckeditor.fields import RichTextField
from django.db.models.deletion import CASCADE

# Create your models here.

MEETING_TYPES = [('PUB', 'Public'), ('SPEC', 'Special'),
                 ('CONF', 'Confidential')]


class Meeting(models.Model):
    title = models.CharField('Meeting Title', max_length=120)
    date = models.DateTimeField('Meeting Date')
    description = models.TextField('Description')

    meeting_type = models.CharField('Meeting Type',
                                    choices=MEETING_TYPES,
                                    max_length=4,
                                    default='PUB')

    def __str__(self) -> str:
        tz = timezone(TIME_ZONE)
        time = self.date.astimezone(tz)
        return f'[{time.strftime("%B %d, %Y %I:%M %p")}] {self.title}'


class Agenda(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=CASCADE)

    def __str__(self) -> str:
        return f'{self.meeting.title} Agenda'


class AgendaItem(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=CASCADE)
    title = models.CharField('Title', max_length=120)
    description = models.TextField('Description')

    POSSIBLE_DECISIONS = [('TBC', 'To be considered'),
                          ('CUC', 'Currently under consideration'),
                          ('A', 'Approved'), ('AWM', 'Approved with motion'),
                          ('R', 'Rejected')]

    result = models.CharField('Result',
                              choices=POSSIBLE_DECISIONS,
                              max_length=3,
                              default='TBC')

    motion = RichTextField('Motion', default="")
    file = models.FileField('Attachment', upload_to="uploads",
                            blank=True)  # temporary

    def __str__(self) -> str:
        return f'[{self.result}] {self.title}'


class Attachment(models.Model):
    agenda_item = models.ForeignKey(AgendaItem, on_delete=CASCADE)
    attachment = models.FileField('File', upload_to="uploads")
    name = models.CharField('Name (optional)',
                            max_length=255,
                            blank=True,
                            default="Untitled File")

    def __str__(self) -> str:
        return f'{self.name} ({os.path.basename(self.attachment.__str__())})'


class MeetingMinutes(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=CASCADE)
    yt_link = models.URLField('Youtube Link', default="", blank=True)
    notes = RichTextField('Notes', blank=True)

    def __str__(self) -> str:
        return f'{self.meeting.title} Minutes'

    class Meta:
        verbose_name = "Meeting Minutes"
        verbose_name_plural = "Meeting Minutes"
