from django.shortcuts import render
import datetime
from meetings import models
import meetings

# Create your views here.
def test_homepage(request):
    agendaitem = models.AgendaItem
    agendaDes = models.AgendaItem.description
    agendaRes = models.AgendaItem.result
    agendaPos = models.AgendaItem.POSSIBLE_DECISIONS
    agendaMotion= models.AgendaItem.motion
    agendaAttach = models.AgendaItem.attachments
    return render(request,'meetings/meetings_homepage.html',{
        'agenda':agendaitem, 
        'description':agendaDes,
        'result': agendaRes,
        'possible':agendaPos,
        'motion':agendaMotion,
        'attached':agendaAttach})