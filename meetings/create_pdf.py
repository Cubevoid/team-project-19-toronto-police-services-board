from typing import List
from meetings.models import *
from pytz import timezone
from tpsb.settings import TIME_ZONE, BASE_DIR
import pdfkit
from django.template import Template, Context
import re, os


def generate_agenda(template: AgendaTemplate,
                    agenda: Agenda,
                    agenda_items: List[AgendaItem],
                    output_path: str = os.path.join(BASE_DIR, "uploads/untitled_agenda.pdf")):
    """
    Generate an agenda PDF.

    :param template: the agenda template
    :param agenda: Agenda model
    :param agenda_items: AgendaItem models
    """
    wk_options = {
        "enable-local-file-access": None,
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
    }

    os.makedirs(os.path.join(BASE_DIR, 'uploads'), exist_ok=True)

    title_page_template = preprocess_html(template.title_page)
    toc_template = preprocess_html(template.contents_header)
    contents_template = re.sub('</?ol>', '', preprocess_html(template.contents_item))  # remove <ol> tags between list items

    agenda_context = Context({
        "title": str(agenda),
        "date": agenda.meeting.date.astimezone(timezone(TIME_ZONE)).strftime("%A %B %d, %Y at %I:%M %p"),
        "recording_link": agenda.meeting.recording_link,
        "description": agenda.meeting.description
    })

    title_page_html = Template(title_page_template).render(agenda_context)
    toc_header_html = Template(toc_template).render(agenda_context)
    contents_html = generate_table_of_contents(Template(contents_template), agenda_items)

    agenda_html = title_page_html + toc_header_html + contents_html

    pdfkit.from_string(agenda_html, output_path=output_path, options=wk_options, css='meetings/agenda.css')


# https://stackoverflow.com/a/39327252/13176711
def newest_file(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    path = max(paths, key=os.path.getctime)
    return os.path.abspath(path)


def preprocess_html(template: str) -> str:
    """
    Preprocess the template by replacing some variables and other fixes for wkhtmltopdf.
    """
    template = re.sub('{{ ?logo ?}}', f'<img src=file://{newest_file("admin-interface/logo")}>', template)
    template = template.replace('<p><!-- pagebreak --></p>',
                                '<p style="page-break-after:always;"><!-- pagebreak --></p>')
    return template


def generate_table_of_contents(template: str, agenda_items: List[AgendaItem]):
    """
    Generates the table of contents list, including sub-items.
    Prerequisites: template is an HTML ordered list.
    """
    contents_html = "<ol>"

    in_subsection = False

    for item in agenda_items:
        # Indent and unindent sub-items correctly
        if item.number % 1 != 0 and not in_subsection:
            in_subsection = True
            contents_html += "<ol>"
        elif item.number % 1 == 0 and in_subsection:
            in_subsection = False
            contents_html += "</ol>"

        item_context = Context({"number": item.number, "title": item.title, "description": item.description})
        contents_html += template.render(item_context) + "\n"

    contents_html += '</ol><p style="page-break-after:always;"><!-- pagebreak --></p>'

    return contents_html