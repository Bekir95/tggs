from django.db import models
from django.utils.formats import date_format
from django.utils.translation import gettext as _

from django.utils import timezone


class Haber(models.Model):

    Baslik = models.CharField(max_length=200 , null=True , blank=True)
    Aciklama = models.TextField(null=True , blank=True)
    Resim = models.ImageField(upload_to='djangouploads/news', null=True , blank=True)
    ana_haber = models.BooleanField(default=False)
    

    def __str__(self):
        return self.Baslik
    


class Duyuru(models.Model):

    Baslik = models.CharField(max_length=200 , null=True , blank=True)
    Aciklama = models.TextField(null=True , blank=True)
    Resim = models.ImageField(upload_to='djangouploads/duyurular', null=True , blank=True)
    date = models.DateField(null=True, blank=True, default=timezone.now)
    

    def __str__(self):
        return self.Baslik
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.date})"
    

import unicodedata

def turkce_upper(metin):
    return (metin
            .replace('i', 'İ')
            .replace('ı', 'I')
            .upper())

class MeclisDokumani(models.Model):
   

    baslik = models.CharField(max_length=255)
    tarih = models.DateField()
    dosya = models.FileField(upload_to='meclis_dokumanlari/', blank=True, null=True)

    class Meta:
        verbose_name = "Meclis Dökümanı"
        verbose_name_plural = "Meclis Dökümanları"
        ordering = ['-tarih']

    def __str__(self):
        ay_yil = date_format(self.tarih, "Y F", use_l10n=True)  # Örn: "Nisan 2025"
        return f"{turkce_upper(ay_yil)} "