from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.hashers import make_password

from artikel.models import Daftar
from users.models import Biodata
import requests

# Create your views here.
def doa(request):
    respnose = requests.get('https://doa-doa-api-ahmadramadhan.fly.dev/api').json()
    return render(request, 'doa.html', {'response':respnose})


def index(request):
    template_name = 'index.html'
    artikel = Daftar.objects.all()
    context = {
        'title' : 'Home!!!',
        'artikel' : artikel,
    }

    return render(request, template_name, context)

    response = request.get('https://doa-doa-api-ahmadramadhan.fly.dev/api')
    data = response.json()
    doa = []
    for dt in data:
        isi = {}
        isi['id'] = dt['attributes']['ID']
        isi['doa'] = dt['attributes']['ID']
        isi['ayat'] = dt['attributes']['ID']
        isi['latin'] = dt['attributes']['ID']
        isi['artinya'] = dt['attributes']['ID']
        doa.append(isi)
    return render(request, 'base.html', {
        'data': doa,
    })


def about(request):
    template_name = 'about.html'
    context = {
        'title' : 'About!!!',
        'nama' : 'disini ada Alief Fajar Gumilang'
    }

    return render(request, template_name, context)

def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    template_name = 'login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('data benar') #data ada di data base
            auth_login(request, user)
            return redirect('index')
        else:
            print('data salah')#data tidak ada

    context = {
        'title' : 'form login'
    }
    return render(request, template_name, context)

def logout_user(request):
    logout(request)
    return redirect('index')

def registrasi(request):
    template_name = "register.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')
        telp = request.POST.get('telp')

        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = nama_depan,
                    last_name = nama_belakang,
                    email = email,
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    alamat = alamat,
                    telp = telp
                )
                return redirect(index)
        except:
            pass

    context = {
        'title':'Resgiter'
    }
    return render(request, template_name, context)