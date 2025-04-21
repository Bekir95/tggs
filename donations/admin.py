from django.contrib import admin
from .models import Bagis,Burs
admin.site.register(Bagis)

# Register your models here.


@admin.register(Burs)
class BursAdmin(admin.ModelAdmin):
    list_display = ('tarih', 'isimsoyisim', 'tc', 'miktar')
    search_fields = ('isimsoyisim', 'tc')



