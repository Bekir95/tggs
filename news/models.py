from django.db import models

class Haber(models.Model):

    Baslik = models.CharField(max_length=200 , null=True , blank=True)
    Aciklama = models.TextField(null=True , blank=True)
    Resim = models.ImageField(upload_to='djangouploads/news', null=True , blank=True)
    Resim2 = models.ImageField(upload_to='djangouploads/news', null=True , blank=True)
    Resim3 = models.ImageField(upload_to='djangouploads/news', null=True , blank=True)
    

    def __str__(self):
        return self.Baslik