"""meetings URL Configuration
"""
from . import views
from django.urls import path, include
from rest_framework import routers
from meetings import views

router = routers.DefaultRouter()
router.register(r'Minutes', views.MMView, 'Minutes')
router.register(r'Meeting', views.MView, 'Meeting')
router.register(r'Agenda', views.AView, 'Agenda')
router.register(r'AgendaItem', views.AIView, 'AgendaItem')

urlpatterns = [
    path('', include(router.urls)),
]
