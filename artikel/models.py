from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length = 40)
    def __str__(self):
        return self.nama

class Daftar(models.Model):
    nama = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.CharField(max_length = 100)
    deskripsi = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)
    # def __str__(self):
    #     return self.nama
