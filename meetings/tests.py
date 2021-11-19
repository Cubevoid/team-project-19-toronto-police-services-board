from django.test import TestCase
from meetings import create_pdf
from meetings.models import *
from datetime import datetime

title_template = """
<br />
<br />
<br />
<h1 style="text-align: center;">{{ logo }}</h1>
<br />
<h1 style="text-align: center;">{{ title }}</h1>
<p></p>
<h2 style="text-align: center;">{{ date }}</h2>
<p><!-- pagebreak --></p>
"""

toc_template = """
<h2 style="text-align: center;">{{ title }}</h2>
<h2 style="text-align: center;">{{ date }}</h2>
<h3 style="text-align: center;">Livestream at: <a href="{{ recording_link }}">{{ recording_link }}</a></h3>
<hr />
<p>{{ description }}</p>
<hr />
<p>{{ table_of_contents }}</p>
"""

content_template = """
<ol>
<li value="{{ number }}. ">{{ title }}<br />{{ description }}</li> <br />
</ol>
"""


# Create your tests here.
class PDFGenerationTestCase(TestCase):

    meeting = Meeting(title='TPSB Nov Test Meeting',
                      date=datetime.now(),
                      description='Test Description',
                      meeting_type='PUB',
                      recording_link='https://youtube.com/')
    agenda = Agenda(meeting=meeting)
    agenda_template = AgendaTemplate(title_page=title_template, toc=toc_template, contents_item=content_template)
    item1 = AgendaItem(agenda=agenda, number=1, title='Agenda Item 1', description='Test Description 1')
    item11 = AgendaItem(agenda=agenda, number=1.1, title='Agenda Item 1.1', description='Test 1.1')
    item2 = AgendaItem(agenda=agenda, number=2, title='Really Long Title ' * 8, description='Test Description 2')

    def test_basic_pdf(self):
        create_pdf.generate_agenda(self.agenda_template, self.agenda, [self.item1, self.item11, self.item2])