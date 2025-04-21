from django.db import models
import os

class Bagis(models.Model):

    Baslik = models.CharField(max_length=200 , null=True , blank=True)
    Aciklama = models.TextField(null=True , blank=True)
    Resim = models.ImageField(upload_to='djangouploads/donations', null=True , blank=True)
    Fiyat = models.IntegerField()

    def __str__(self):
        return self.Baslik
    



class Burs(models.Model):
    tarih = models.DateField()
    tc = models.CharField(max_length=11)
    isimsoyisim = models.CharField(max_length=100)
    miktar = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.isimsoyisim
    



class BursExcel(models.Model):
    excel_file = models.FileField(upload_to='excel_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Excel File uploaded at {self.uploaded_at}"

    def save(self, *args, **kwargs):
        # Eğer bir dosya varsa, eski dosyayı sil
        if self.pk:
            old_file = BursExcel.objects.get(pk=self.pk).excel_file
            if old_file != self.excel_file:
                if os.path.isfile(old_file.path):
                    os.remove(old_file.path)
        super().save(*args, **kwargs)