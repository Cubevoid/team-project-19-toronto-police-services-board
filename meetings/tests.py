from django.test import TestCase
from meetings import create_pdf
from meetings.models import *
from datetime import datetime


# Create your tests here.
class PDFGenerationTestCase(TestCase):

    meeting = Meeting(title='TPSB Nov Test Meeting',
                      date=datetime.now(),
                      description='Test Description',
                      meeting_type='PUB')
    agenda = Agenda(meeting=meeting)

    def test_basic_pdf(self):
        create_pdf.generate_agenda(self.agenda, [])