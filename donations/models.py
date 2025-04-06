from django.db import models

class Bagis(models.Model):

    Baslik = models.CharField(max_length=200 , null=True , blank=True)
    Aciklama = models.TextField(null=True , blank=True)
    Resim = models.ImageField(upload_to='djangouploads/donations', null=True , blank=True)
    Fiyat = models.IntegerField()

    def __str__(self):
        return self.Baslik