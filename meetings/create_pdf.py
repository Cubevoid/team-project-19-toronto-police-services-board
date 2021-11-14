from os import path
from fpdf import FPDF
from typing import List
from meetings.models import *
from pytz import timezone
from tpsb.settings import TIME_ZONE, BASE_DIR

AUTHOR = 'Toronto Police Services Board'
MARGIN_SIZE_MM = 25.4
LETTER_WIDTH_MM = 8.5 * 25.4


def generate_agenda(agenda: Agenda, agenda_items: List[AgendaItem]):
    pdf = PDF(format='Letter', unit='mm')

    # 1 inch margins
    pdf.set_top_margin(MARGIN_SIZE_MM)
    pdf.set_left_margin(MARGIN_SIZE_MM)
    pdf.set_right_margin(MARGIN_SIZE_MM)

    pdf.set_agenda(agenda)
    pdf.set_agenda_items(agenda_items)
    pdf.set_author(AUTHOR)
    # pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_c1.txt')
    pdf.print_title_page()
    pdf.output('test.pdf', 'F')


class PDF(FPDF):

    def set_agenda(self, agenda: Agenda):
        self.title = str(agenda)
        self.set_subject(agenda.meeting.description)
        self.date = agenda.meeting.date

    def set_agenda_items(self, agenda_items):
        self.agenda_items = agenda_items

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

    def print_title_page(self):
        self.add_page()

        logo = newest_file(os.path.join(BASE_DIR, 'admin-interface/logo/'))
        width = 50
        x = (LETTER_WIDTH_MM - width) / 2
        self.image(logo, x=x, w=width, h=width)

        # Arial bold 15
        self.set_font('Arial', 'B', 16)
        # Calculate width of title and position
        w = self.get_string_width(self.title)
        self.set_y(width + 40)
        self.set_x((LETTER_WIDTH_MM - w) / 2)
        # Title
        self.cell(w=w, txt=self.title, ln=2, align='C')
        self.ln(10)

        tz = timezone(TIME_ZONE)
        time = self.date.astimezone(tz)
        time_formatted = time.strftime("%A %B %d, %Y at %I:%M %p")
        self.set_font('Arial', 'B', 12)
        w = self.get_string_width(time_formatted)
        self.set_x((LETTER_WIDTH_MM - w) / 2)
        # Date and time
        self.cell(w=w, h=9, txt=time_formatted, ln=2, align='C')


# https://stackoverflow.com/a/39327252/13176711
def newest_file(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)