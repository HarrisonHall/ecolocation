from django.http import HttpResponse
from ecolocation.models import Event, Tag
from django.shortcuts import render

from ecolocation.forms import EventForm
from django.forms import modelformset_factory, ModelForm, inlineformset_factory

import datetime

import pandas as pd
import random
import os 


def create_event(request):
    g = Event.objects.all()
    context = {"event_table": EventForm, "all_events": g,}
    return render(request, 'events/make_event.html', context)

def make_event(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST["name"]
        print(request.POST["lat"], request.POST["lon"])
        lat = float(request.POST["lat"])
        lon = float(request.POST["lon"])
        print(lat, lon)
        num_joined = 0
        radius = float(request.POST["radius"])
        start_time = datetime.datetime.strptime(request.POST["start_time"], "%Y-%m-%d")
        end_time = datetime.datetime.strptime(request.POST["end_time"], "%Y-%m-%d")
                
        new_event = Event(name=name, lat=lat, lon=lon, num_joined=num_joined,start_time=start_time,end_time=end_time,radius=radius)
        new_event.save()
        context = {"lat": lat, "lon": lon}
        return render(request, "events/confirm_event.html", context)
        #return render(request, "home.html", {})
    return HttpResponse("Bad.")


def check_event2(request):
    print(request.POST)
    lat = 0
    lon = 0
    if request.method == "POST":
        print(request.POST)
        try:
            lat = float(request.POST['lat'])
            lon = float(request.POST['lon'])
        except:
            context = {'error': "Geolocation error."}
            return render(request, 'events/check_event.html', context)
        in_event = False
        event_name = ""
        for event in Event.objects.all():
            print(event.close_enough(lat,lon), event.event_is_now())
            if event.close_enough(lat, lon) and event.event_is_now():
                in_event = True
                print("Near Event.")
                date = datetime.date.today()
                user = request.user
                bat_id = random.randint(69,420)
                bat_name = random_bat()
                new_tag = Tag(user=user, date=date, bat_id=bat_id, bat_name=bat_name, event=event.name)
                new_tag.save()
                event_name = event.name
            else:
                print("Not Near Event.")
        if in_event:
            context = {
                "lat": lat,
                "lon": lon,
                "event": event_name,
            }
            return render(request, "events/at_event.html",context)
        return HttpResponse("Not at any events.")
    return HttpResponse("Bad.")

def check_event(request):
    g = Event.objects.all()
    context = {"event_table": EventForm, "all_events": g,}
    return render(request, 'events/check_event.html', context)

def view_tags(request):
    g = Tag.objects.all()
    for i in g:
        print(i.user)
    context = {"tags": g}
    return render(request, 'tags/check_tags.html', context)

def view_tags_single(request):
    g = Tag.objects.all().filter(user=request.user)
    bat = get_bat_data_dict()
    desc = []
    images = []
    colors = []
    prob = []
    
    for i in g:
        desc.append(bat[i.bat_name]["description"])
        images.append(bat[i.bat_name]["image"])
        colors.append(bat[i.bat_name]["HexColor"])
        prob.append(bat[i.bat_name]["Probability"])
    
    context = {"tags": zip(g, desc, images, colors, prob)}
    return render(request, 'tags/check_tags.html', context)

def Test(request):
    print(get_bat_data)
    return HttpResponse("Test")

def get_bat_data():
    return pd.read_csv("bats/bat_types.csv")

def get_bat_data_dict():
    data = pd.read_csv("bats/bat_types.csv")
    good_data = {}

    for i in range(len(data)):
        print(os.path.exists(os.getcwd()+"/images/Fruit.png"))
        good_data[data["Type"][i]] = {
            #"image": os.path.dirname(os.path.realpath(__file__)) + data["Image"][i][1:],
            "image": data["Image"][i][2:],
            "description": data["Description"][i].replace("|",","),
            "HexColor": data["HexColor"][i],
            "Probability": str(float(data["Probability"][i])*100)+"%",
        }
    return good_data

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
    
