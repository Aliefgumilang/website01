from django.contrib import admin
from django.urls import path, include
from website.views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dashboard/', include('artikel.urls')),
    path('about', about, name='about'),
    path('artikel/', include('artikel.urls')),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', registrasi, name='register'),
    path('doa', views.doa, name='doa'),
]
