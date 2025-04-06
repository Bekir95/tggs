from django.shortcuts import render
from .models import Activities,MainPageInner

def home(request):
    data = { 
        'activities' : Activities.objects.all(),
        'whoWeR' : MainPageInner.objects.first()
    }

    print(data['whoWeR'].biz_kimiz)

    return render(request , 'index.html',data)
def contact(request):

    return render(request , 'contact.html')
