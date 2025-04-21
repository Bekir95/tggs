from django.urls import path
from .views import *

urlpatterns = [
    path('kurumsal' , kurumsal , name='company'),
    path('yonetim-kurulu' , yk , name='yonetim-kurulu'),
    path('il-baskanliklari' , cities , name='il-baskanliklari'),
    path('insan-kaynaklari' , ik , name='insan-kaynaklari'),
    path('hakkimizda' , hakkimizda , name='hakkimizda'),
    path('bio/<str:name>' , bio , name='bio'),
    path('iller/<str:city>' , ib , name='ib'),
    path('politikalar' , pltk , name='pltk'),
    path('genelbaskanlik', organizational_units_view, name='organizational_units'),
    path('organizasyon/<int:unit_id>/', organizational_unit_detail_view, name='organizational_unit_detail'),  # Detay sayfası
    path('idari-yapı/', organization_tree, name='organization-tree'),

]