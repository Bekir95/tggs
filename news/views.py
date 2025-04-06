from django.shortcuts import render

from .models import Haber

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