from django.urls import path
from .views import news , new
urlpatterns = [
    path('' , news , name='news'),
    path('/<int:pk>' , new , name='new'),
]