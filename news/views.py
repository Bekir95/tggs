from django.shortcuts import render

from .models import Haber, Duyuru, Event, MeclisDokumani
from collections import defaultdict
import json

# Create your views here.
def news(request):
    data = { 
        'news' : Haber.objects.all()
    }
    return render(request , 'news.html' , data)

def new(request , pk):
    data = {
        'new' : Haber.objects.get(id=pk)
    }
    return render(request , 'new.html' , data)


# Create your views here.
def duyurular(request):
    data = { 
        'news' : Duyuru.objects.all()
    }
    return render(request , 'duyurular.html' , data)

def duyuru(request , pk):
    data = {
        'new' : Duyuru.objects.get(id=pk)
    }
    return render(request , 'duyuru.html' , data)


def takvim(request):
    # Tüm etkinlikleri çek
    events = Event.objects.all()
    # Yıl-ay bazında gruplama
    grouped = defaultdict(list)
    for e in events:
        key = e.date.strftime('%Y-%m')
        grouped[key].append({'day': e.date.day, 'title': e.title})
    # JSON’a çevir
    events_json = json.dumps(grouped)
    
    return render(request, 'takvim.html', {
        'events_json': events_json
    })


def meclis(request):
    data = {
        'news' : MeclisDokumani.objects.all()
    }
    return render(request , 'meclis.html' , data)