from django.contrib import admin
from .models import *

admin.site.register(YonetimKurulu)
admin.site.register(InsanKaynaklari)
admin.site.register(Il)
admin.site.register(Ilce)
admin.site.register(Il_Baskanligi)
admin.site.register(Ilce_Baskanligi)

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    # Arama yapılabilecek alanları belirtin
    search_fields = ['full_name', 'title']

admin.site.register(Person, PersonAdmin)

@admin.register(OrganizationalUnit)
class OrganizationalUnitAdmin(admin.ModelAdmin):
    list_display = ('indented_name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)

    def indented_name(self, obj):
        level = 0
        current = obj
        while current.parent:
            level += 1
            current = current.parent
        return f"{'— ' * level}{obj.name}"
    indented_name.short_description = 'Birim Adı (Hiyerarşi)'