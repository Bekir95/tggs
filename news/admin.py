from django.contrib import admin

from .models import Haber,Duyuru,Event,MeclisDokumani


admin.site.register(Duyuru)
admin.site.register(Event)
admin.site.register(MeclisDokumani)
# Register your models here.

class HaberAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        # Eğer is_active alanı True ise
        if obj.ana_haber:
            # Diğer tüm öğelerin is_active alanlarını False yap
            Haber.objects.exclude(id=obj.id).update(ana_haber=False)
        super().save_model(request, obj, form, change)

admin.site.register(Haber, HaberAdmin)