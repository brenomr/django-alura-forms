"""
URL resolver for tickets app
"""

from django.urls import path
from tickets.views import index, check_trip_details

urlpatterns = [
    path('', index, name='index'),
    path('check_trip_details', check_trip_details, name='check_trip_details'),
]
