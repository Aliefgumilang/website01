from django.contrib import admin
from artikel.models import *

# Register your models here.

admin.site.register(Kategori)

class DaftarAdmin(admin.ModelAdmin):
    list_display = ['nama','judul','deskripsi','kategori']
admin.site.register(Daftar, DaftarAdmin)