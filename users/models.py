from django.db import models
from django.contrib.auth.models import User


class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField()
    telp = models.CharField(max_length = 14)

    def __str__(self):
        return "{} - {}".format(self.user, self.telp)

class Users(models.Model):
    username = models.CharField(max_length = 20)
    email = models.EmailField()
    # staff = models.ForeignKey()

    def __str__(self):
        return "{} - {}".format(self.username, self.email)