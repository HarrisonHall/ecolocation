from django.http import HttpResponse
from ecolocation.models import Event, Tag
from django.shortcuts import render

from ecolocation.forms import EventForm
from django.forms import modelformset_factory, ModelForm, inlineformset_factory

import datetime

import pandas as pd
import random


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
                print("Near Event.")
                date = datetime.date.today()
                user = request.user
                bat_id = random.randint(69,420)
                bat_name = random_bat()
                new_tag = Tag(user=user, date=date, bat_id=bat_id, bat_name=bat_name, event=event.name)
                new_tag.save()
            else:
                print("Not Near Event.")
        return HttpResponse("Not at any events.")
    return HttpResponse("Bad.")

def view_tags(request):
    g = Tag.objects.all()
    for i in g:
        print(i.user)
    context = {"tags": g}
    return render(request, 'tags/check_tags.html', context)

def view_tags_single(request):
    g = Tag.objects.get(user=request.user)
    print(type(g))
    for i in g:
        print(i.user)
    context = {"tags": g}
    return render(request, 'tags/check_tags.html', context)

def Test(request):
    print(get_bat_data)
    return HttpResponse("Test")

def get_bat_data():
    return pd.read_csv("bats/bat_types.csv")

def random_bat():
    #Tag.objects.all().delete()
    bats = get_bat_data()
    weights = []
    for i in range(len(bats)):
        print(bats["Type"][i])
        weights += [bats['Type'][i]]*int(float(bats['Probability'][i])*100)
    print(weights)
    print(random.choice(weights))
    return random.choice(weights)
    
