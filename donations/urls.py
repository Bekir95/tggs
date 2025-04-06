from django.urls import path
from .views import donations , donation

urlpatterns = [
    path('bagislar' , donations , name='donations'),
    path('bagislar/<int:id>' , donation , name='donation')
]