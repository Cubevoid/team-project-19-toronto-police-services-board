"""meetings URL Configuration
"""
from . import views
from django.urls import path, include 
from rest_framework import routers
from meetings import views

router = routers.DefaultRouter()
router.register(r'MeetingMinutes', views.MMView, 'MeetingMinutes')

urlpatterns = [
    path('api/', include(router.urls)),
]
