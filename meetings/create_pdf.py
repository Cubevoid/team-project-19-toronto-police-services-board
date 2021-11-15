from os import path
from fpdf import FPDF
from typing import List
from meetings.models import *
from pytz import timezone
from tpsb.settings import TIME_ZONE, BASE_DIR

AUTHOR = 'Toronto Police Services Board'
MARGIN_SIZE_MM = 25.4
LETTER_WIDTH_MM = 8.5 * 25.4
INDENT_AMOUNT = 8
LINE_SPACING = 8
FONT_FAMILY = 'Arial'


def generate_agenda(agenda: Agenda, agenda_items: List[AgendaItem]):
    pdf = PDF(format='Letter', unit='mm')

    # 1 inch margins
    pdf.set_top_margin(MARGIN_SIZE_MM)
    pdf.set_left_margin(MARGIN_SIZE_MM)
    pdf.set_right_margin(MARGIN_SIZE_MM)

    pdf.set_agenda(agenda)
    pdf.set_agenda_items(agenda_items)
    pdf.set_author(AUTHOR)
    pdf.print_title_page()
    pdf.print_contents()
    pdf.output('test.pdf', 'F')


class PDF(FPDF):

    def set_agenda(self, agenda: Agenda):
        self.title = str(agenda)
        self.set_subject(agenda.meeting.description)
        self.date = agenda.meeting.date
        self.agenda = agenda

    def set_agenda_items(self, agenda_items):
        self.agenda_items = agenda_items

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font(FONT_FAMILY, 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def __print_content(self, agenda_item: AgendaItem):
        self.set_font(family=FONT_FAMILY, size=12)

        # Indent sub-items
        if agenda_item.number % 1 != 0:
            self.cell(w=INDENT_AMOUNT + self.get_string_width('1. '), h=LINE_SPACING)

        num = f'{agenda_item.number}. '
        self.cell(w=self.get_string_width(num), h=LINE_SPACING, txt=num)
        self.cell(w=INDENT_AMOUNT, h=LINE_SPACING)

        w = LETTER_WIDTH_MM
        w -= 60 if agenda_item.number % 1 == 0 else INDENT_AMOUNT + 60
        self.multi_cell(w=w, h=LINE_SPACING, txt=f'{agenda_item.title}\n{agenda_item.description}', align='L')

    def print_contents(self):
        self.add_page()

        # Arial bold 15
        self.set_font(FONT_FAMILY, 'B', 16)
        # Calculate width of title and position
        w = self.get_string_width(self.title)
        self.set_x((LETTER_WIDTH_MM - w) / 2)
        # Title
        self.cell(w=w, h=LINE_SPACING, txt=self.title, ln=2, align='C')

        tz = timezone(TIME_ZONE)
        time = self.date.astimezone(tz)
        time_formatted = time.strftime("%A %B %d, %Y at %I:%M %p")
        self.set_font(FONT_FAMILY, 'B', 12)
        w = self.get_string_width(time_formatted)
        self.set_x((LETTER_WIDTH_MM - w) / 2)
        # Date and time
        self.cell(w=w, h=LINE_SPACING, txt=time_formatted, ln=2, align='C')

        if self.agenda.meeting.recording_link:
            w = self.get_string_width(f'Livestream at: {self.agenda.meeting.recording_link}')
            self.set_x((LETTER_WIDTH_MM - w) / 2)
            # Non-link part
            self.cell(w=self.get_string_width('Livestream at: '), h=LINE_SPACING, txt='Livestream at: ', align='C')
            # Hyperlink part
            self.set_text_color(r=0, g=0, b=255)
            self.set_font(FONT_FAMILY, 'UB', 12)
            self.cell(w=w,
                      h=LINE_SPACING,
                      txt=self.agenda.meeting.recording_link,
                      ln=2,
                      align='L',
                      link=self.agenda.meeting.recording_link)
            self.set_text_color(r=0)  # Reset to black
        self.ln(LINE_SPACING / 2)
        self.line(50, self.get_y(), LETTER_WIDTH_MM - 50, self.get_y())
        self.ln(LINE_SPACING / 2)

        for agenda_item in self.agenda_items:
            self.__print_content(agenda_item)
            self.ln(LINE_SPACING / 2)

    def print_title_page(self):
        self.add_page()

        logo = newest_file(os.path.join(BASE_DIR, 'admin-interface/logo/'))
        width = 50
        x = (LETTER_WIDTH_MM - width) / 2
        self.image(logo, x=x, w=width, h=width)

        # Arial bold 15
        self.set_font(FONT_FAMILY, 'B', 16)
        # Calculate width of title and position
        w = self.get_string_width(self.title)
        self.set_y(width + 40)
        self.set_x((LETTER_WIDTH_MM - w) / 2)
        # Title
        self.cell(w=w, txt=self.title, h=LINE_SPACING, ln=2, align='C')
        self.ln(LINE_SPACING)

        tz = timezone(TIME_ZONE)
        time = self.date.astimezone(tz)
        time_formatted = time.strftime("%A %B %d, %Y at %I:%M %p")
        self.set_font(FONT_FAMILY, 'B', 12)
        w = self.get_string_width(time_formatted)
        self.set_x((LETTER_WIDTH_MM - w) / 2)
        # Date and time
        self.cell(w=w, h=LINE_SPACING, txt=time_formatted, ln=2, align='C')


# https://stackoverflow.com/a/39327252/13176711
def newest_file(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)