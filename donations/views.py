from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Bagis,Burs
import openpyxl
from django.http import HttpResponse
from django.template import Library
# Templatetag'leri yükle
from donations.templatetags.mask_filters import mask_tc, mask_name

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

def donationNews(request):
    
    burslar = Burs.objects.order_by('-tarih')  # En günceli en üstte
    paginator = Paginator(burslar, 7)  # Sayfa başına 10 kayıt
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'donation-news.html', {'page_obj': page_obj})


def burs_excel_export(request):
    burslar = Burs.objects.all().order_by('-tarih')

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Verilen Burslar"

    # Başlık satırı
    ws.append(["Tarih", "TC", "İsim Soyisim", "Miktar"])

    for burs in burslar:
        # Maskelenmemiş verileri dışarı aktar
        # Maskeleme işlemlerini burada yap
        masked_tc = mask_tc(burs.tc)
        masked_name = mask_name(burs.isimsoyisim)
        ws.append([str(burs.tarih), masked_tc, masked_name, burs.miktar])

    # HTTP response
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = 'attachment; filename=burslar.xlsx'
    wb.save(response)
    return response
