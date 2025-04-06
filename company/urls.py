from django.urls import path
from .views import kurumsal , yk , hakkimizda , cities , bio , ib , ik, pltk
urlpatterns = [
    path('kurumsal' , kurumsal , name='company'),
    path('yonetim-kurulu' , yk , name='yonetim-kurulu'),
    path('il-baskanliklari' , cities , name='il-baskanliklari'),
    path('insan-kaynaklari' , ik , name='insan-kaynaklari'),
    path('hakkimizda' , hakkimizda , name='hakkimizda'),
    path('bio/<str:name>' , bio , name='bio'),
    path('iller/<str:city>' , ib , name='ib'),
    path('politikalar' , pltk , name='pltk'),
]