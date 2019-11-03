from django.http import HttpResponse
from ecolocation.models import Event
from django.shortcuts import render

from ecolocation.forms import EventForm
from django.forms import modelformset_factory, ModelForm, inlineformset_factory

import datetime

import pandas


def create_event(request):
    g = Event.objects.all()
    context = {"event_table": EventForm, "all_events": g,}
    return render(request, 'events/make_event.html', context)

def make_event(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST["name"]
        lat = float(request.POST["lat"])
        lon = float(request.POST["lon"])
        num_joined = 0
        radius = float(request.POST["radius"])
        start_time = datetime.datetime.strptime(request.POST["start_time"], "%Y-%m-%d")
        end_time = datetime.datetime.strptime(request.POST["end_time"], "%Y-%m-%d")
                
        new_event = Event(name=name, lat=lat, lon=lon, num_joined=num_joined,start_time=start_time,end_time=end_time,radius=radius)
        new_event.save()
        return HttpResponse("Good.")
    return HttpResponse("Bad.")

def check_event2(request):
    print(request.POST)
    lat = 0
    lon = 0
    if request.method == "POST":
        print(request.POST)
        lat = float(request.POST['lat'])
        lon = float(request.POST['lon'])
        for event in Event.objects.all():
            if event.close_enough(lat, lon) and event.event_is_now():
                print("YO")
            else:
                print("NO")
        return HttpResponse("Not at any events.")
    return HttpResponse("Bad.")

def Test(request):
    return HttpResponse("Test")
