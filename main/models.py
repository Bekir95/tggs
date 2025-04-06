from django.db import models

# Create your models here.
class MainPageInner(models.Model):
    biz_kimiz = models.TextField(null=True , blank=True)

class Activities(models.Model):
    Baslik = models.CharField(max_length=200 , null=True , blank=True)
    Aciklama = models.TextField(null=True , blank=True)
    Resim = models.ImageField(upload_to='djangouploads/mainActivities', null=True , blank=True)
