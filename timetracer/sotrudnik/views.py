from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required


def sotrudnik(request):
    return render(request, 'sotrudnik/sotrudnik.html')

# def calendar(request):
#     return render(request, 'sotrudnik/calendar.html')


def calendar_view(request):
    events = Event.objects.filter(created_by=request.user)
    return render(request, 'sotrudnik/calendar.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('calendar_view')
    else:
        form = EventForm()
    return render(request, 'sotrudnik/event_form.html', {'form': form})


