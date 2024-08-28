""" Tickets Form """

from django import forms

class TicketsForm(forms.Form):
    """ View responsible to Manage Tickets """
    origin = forms.CharField(label='Origin', max_length=200)
    destination = forms.CharField(label='Destination', max_length=200)
    departure_date = forms.DateField(label='Departure Date')
    return_date = forms.DateField(label='Return Date')
