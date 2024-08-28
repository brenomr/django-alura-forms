from django.shortcuts import render

from tickets.forms import TicketsForm

def index(request):
    form = TicketsForm()
    context = {
        'form': form
    }
    return render(request, 'tickets/index.html', context=context)

def check_trip_details(request):
    if(request.method == 'POST'):
        form = TicketsForm(request.POST)
        context = { 'form': form }
        return render(request, 'tickets/check_trip_details.html', context=context)
