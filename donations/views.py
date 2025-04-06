from django.shortcuts import render
from .models import Bagis
def donations(request):

    data = { 
        'donations' : Bagis.objects.all()
    }
    
    return render(request,'donations.html' , data)

def donation(request,id):
    data = {
        'donation' : Bagis.objects.get(id=id)
    }
    return render(request , 'donation.html' , data)