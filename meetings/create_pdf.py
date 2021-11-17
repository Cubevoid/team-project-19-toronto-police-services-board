from os import path
from typing import List
from meetings.models import *
from pytz import timezone
from tpsb.settings import TIME_ZONE, BASE_DIR
import pdfkit

AUTHOR = 'Toronto Police Services Board'


def generate_agenda(template: str, agenda: Agenda, agenda_items: List[AgendaItem]):
    """
    Generate an agenda PDF.

    :param template: the file path of the HTML template
    :param agenda: Agenda model
    :param agenda_items: AgendaItem models
    """
    with open(template, 'r') as file:
        document = file.read()

    document = document.replace('{ logo }', f'<img src=file://{newest_file("admin-interface/logo")}>')
    document = document.replace('{ title }', str(agenda))

    tz = timezone(TIME_ZONE)
    time = agenda.meeting.date.astimezone(tz)
    time_formatted = time.strftime("%A %B %d, %Y at %I:%M %p")

    document = document.replace('{ date }', time_formatted)

    options = {
        "enable-local-file-access": None
    }
    pdfkit.from_string(document, output_path='./test.pdf', verbose=True, options=options)
    pass


# https://stackoverflow.com/a/39327252/13176711
def newest_file(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    path = max(paths, key=os.path.getctime)
    return os.path.abspath(path)