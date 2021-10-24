from django.db import models


# Create your models here.

class AgendaItem(models.Model):
    title = models.CharField('Title', max_length=120)
    description = models.TextField('Description')

    POSSIBLE_DECISIONS = [('TBC', 'To be considered'),
                          ('CUC', 'Currently under consideration'),
                          ('A', 'Approved'), 
                          ('AWM', 'Approved with motion'),
                          ('R', 'Rejected')]

    result = models.CharField('Result',
                              choices=POSSIBLE_DECISIONS,
                              max_length=3,
                              default='TBC')
    
    motion = models.TextField('Motion')
    attachments = models.FileField('Attachments')  # only one file is supported for now

    def __str__(self) -> str:
        return f'[{self.result}] {self.title}'


class Agenda(models.Model):
    title = models.CharField('Title', max_length=120)
    description = models.TextField('Description')

    MEETING_TYPES = [('PUB', 'Public'), ('SPEC', 'Special'),
                     ('CONF', 'Confidential')]

    meeting_type = models.CharField('Meeting Type',
                                    choices=MEETING_TYPES,
                                    max_length=4,
                                    default='PUB')

    items = models.ManyToManyField(AgendaItem, verbose_name='Agenda Items')


class MeetingMinutes(models.Model):
    title = models.CharField('Title', max_length=120)
    date = models.DateField('Date')
    description = models.TextField('Description')
    yt_link = models.URLField('Youtube Link', default="")
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    notes = models.TextField('Notes')

    def __str__(self) -> str:
        return self.title

