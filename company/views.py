from django.shortcuts import render, get_object_or_404
from company.models import *

def kurumsal(request):
    return render(request , 'kurumsal.html')

def yk(request):
    context = {
        'yon_kur': YonetimKurulu.objects.all()
    }
    return render(request , 'yk.html',context)

def hakkimizda(request):
    return render(request, 'hakkimizda.html')

def cities(request):
    return render(request , 'cities.html')

def bio(request , name):
    return render(request , 'bio.html')

def ib(request , city):
    kisiler = Il_Baskanligi.objects.filter(Yonetici_Il__Sehir_Ismi__iexact=city.lower())
    context = {
        'kisiler' : kisiler,
        'city' : city.upper()
    }
    return render(request , 'ib.html',context)

def ik(request ):
    context = {
        'ins_kay': InsanKaynaklari.objects.all()
    }
    return render(request , 'ik.html',context)


def pltk(request ):
    return render(request , 'politikalar.html')






from django.shortcuts import render
from .models import OrganizationalUnit

def organizational_units_view(request):
    organizational_units = OrganizationalUnit.objects.filter(parent=None)
    units_data = []

    for unit in organizational_units:
        sub_units = OrganizationalUnit.objects.filter(parent=unit)
        people = unit.people.all()  # Bu birime bağlı kişiler
        units_data.append({
            'unit': unit,
            'sub_units': sub_units,
            'people': people
        })

    context = {
        'units_data': units_data
    }
    return render(request, 'organizational_units.html', context)

def organizational_unit_detail_view(request, unit_id):
    # Belirli bir organizasyon birimini ID'ye göre al
    unit = get_object_or_404(OrganizationalUnit, id=unit_id)
    
    # Alt birimlerini al
    sub_units = OrganizationalUnit.objects.filter(parent=unit)

    context = {
        'unit': unit,
        'sub_units': sub_units
    }

    return render(request, 'organizational_unit_detail.html', context)




def organization_tree(request):
    units = OrganizationalUnit.objects.all()

    def build_tree(unit):
        children = OrganizationalUnit.objects.filter(parent=unit)
        children_data = []
        for child in children:
            children_data.append({
                'id': child.id,
                'name': child.name,
                'children': build_tree(child),  # Alt birimleri yinele
                'personnel': [{'full_name': person.full_name, 'title': person.title} for person in unit.people.all()]  # Personel bilgilerini al
            })
        return children_data

    # Ana birimler
    tree_data = []
    for unit in units.filter(parent__isnull=True):  # Ana birimler
        tree_data.append({
            'id': unit.id,
            'name': unit.name,
            'children': build_tree(unit),  # Alt birimleri al
            'personnel': [{'full_name': person.full_name, 'title': person.title} for person in unit.people.all()]  # Personel bilgilerini al
            
        })
    


    return render(request, 'organization_tree.html', {'tree_data': tree_data})
