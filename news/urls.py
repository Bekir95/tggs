from django.urls import path
from .views import news , new, duyurular, duyuru,takvim,meclis
urlpatterns = [
    path('faaliyetlerimiz' , news , name='news'),
    path('faaliyetlerimiz/<int:pk>' , new , name='new'),
    path('duyurular' , duyurular , name='duyurular'),
    path('duyuru/<int:pk>' , duyuru , name='duyuru'),
    path('takvim' , takvim , name='takvim'),
    path('meclis' , meclis , name='meclis'),
]