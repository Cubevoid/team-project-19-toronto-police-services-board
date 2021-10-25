"""meetings URL Configuration
"""
from . import views
from django.urls import path

urlpatterns = [
    path('test/', views.current_datetime)
]
