"""meetings URL Configuration
"""
from . import views
from django.urls import path, include
from rest_framework import routers
from meetings import views
from rest_framework_extensions.routers import NestedRouterMixin

router = routers.DefaultRouter()
router.register(r'Minutes', views.MMView, 'Minutes')
router.register(r'PrivateMeeting', views.PMView, 'PrivateMeeting')
router.register(r'Meeting', views.MView, 'meeting')
router.register(r'Agenda', views.AView, 'Agenda')
router.register(r'AgendaItem', views.AIView, 'AgendaItem')

class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

meeting_router = router.register(r'Meeting', views.MView, 'meeting')
meeting_router.register(
    r'Agenda',
    views.AView,
    basename='meeting-agenda',
    parents_query_lookups=['meeting']
).register(
    'AgendaItem',
    views.AIView,
    basename='meeting-agenda-agendaitem',
    parents_query_lookups=['agenda','agenda_id']
)
meeting_router.register(
    'Minutes',
    views.MMView,
    basename='meeting-minutes',
    parents_query_lookups=['meeting']
)

private_meeting_router = router.register(r'PrivateMeeting', views.PMView, 'PrivateMeeting')
private_meeting_router.register(
    'Agenda',
    views.AView,
    basename='pmeeting-agenda',
    parents_query_lookups=['meeting']
).register(
    'AgendaItem',
    views.AIView,
    basename='pmeeting-agenda-agendaitem',
    parents_query_lookups=['agenda','agenda_id']
)
private_meeting_router.register(
    'Minutes',
    views.MMView,
    basename='pmeeting-minutes',
    parents_query_lookups=['meeting']
)


urlpatterns = [
    path('', include(router.urls)),
]
