from django.urls import path
from .views import donationNews, donations , donation,burs_excel_export

urlpatterns = [
    path('bagislar' , donations , name='donations'),
    path('bagislar/<int:id>' , donation , name='donation'),
    path('bagislar-duyuru' , donationNews , name='donation-news'),
    path('burslar/excel/', burs_excel_export, name='burs_excel_export'),
]