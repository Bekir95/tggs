from django.urls import path
from django.views.generic import TemplateView
from .views import home , contact,updated
urlpatterns = [
    path("", home , name='home'),
    path("iletisim", contact , name='contact'),
    path("guncel", updated , name='updated'),
]