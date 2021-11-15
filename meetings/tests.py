from django.test import TestCase
from meetings import create_pdf
from meetings.models import *
from datetime import datetime


# Create your tests here.
class PDFGenerationTestCase(TestCase):

    meeting = Meeting(title='TPSB Nov Test Meeting',
                      date=datetime.now(),
                      description='Test Description',
                      meeting_type='PUB',
                      recording_link='https://youtube.com/')
    agenda = Agenda(meeting=meeting)
    item1 = AgendaItem(agenda=agenda, number=1, title='Agenda Item 1', description='Test Description 1')
    item11 = AgendaItem(agenda=agenda, number=1.1, title='Agenda Item 1.1', description='Test 1.1')
    item2 = AgendaItem(agenda=agenda, number=2, title='Really Long Title ' * 8, description='Test Description 2')

    def test_basic_pdf(self):
        create_pdf.generate_agenda(self.agenda, [self.item1, self.item11, self.item2])