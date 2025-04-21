from django.shortcuts import render
from .models import Activities,MainPageInner
from news.models import Haber,Duyuru

def home(request):


    ana_haber = Haber.objects.filter(ana_haber=True)
    alt_haberler =  Haber.objects.filter(ana_haber=False)[:3]
    duyurular = Duyuru.objects.all()

    data = { 
        'activities' : Haber.objects.all(),
        'whoWeR' : MainPageInner.objects.first(),
        'ana_haber' : ana_haber,
        'alt_haberler' : alt_haberler,
        'duyurular' : duyurular
    }

    

    return render(request , 'index.html',data)


def contact(request):

    return render(request , 'contact.html')


def updated(request):

    return render(request , 'guncel.html')
