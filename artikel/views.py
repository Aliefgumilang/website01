from django.shortcuts import render, redirect
from artikel.models import *
from django.http import request
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .forms import DaftarForms


def is_operator(user):
    if user.groups.filter(name='operator').exists():
        
        return True
    else:
        return False


@login_required
def list_artikel(request):
    template_name = 'list_artikel.html'
    artikel_list = Daftar.objects.filter(nama = request.user)
    context = {
        'title' : 'Halaman Artikel',
        'artikel' : artikel_list
    }

    return render(request, template_name, context)


@login_required
@user_passes_test(is_operator)
def users(request):
    if request.user.groups.filter(name='operator').exists():
        request.session['is_operator'] = 'operator'

    template_name = 'dashboard.html'
    list_user = User.objects.all()
    context = {
        'title' : 'Users',
        'list_user' : list_user
    }

    return render(request, template_name, context)

@login_required
def add_artikel(request):
    template_name = 'add_artikel.html'
    kategori = Kategori.objects.all()
    
    if request.method == "POST":
        forms_daftar = DaftarForms(request.POST)
        if forms_daftar.is_valid():
           art = forms_daftar.save(commit=False)
           art.nama = request.user
           art.save()
        
        return redirect(list_artikel)
    else:
        forms_daftar = DaftarForms()
    context = {
        'title' : 'Tambah Artikel',
        'kategori' : kategori,
        'forms_daftar' : forms_daftar
    }
    return render(request, template_name, context)

@login_required
def update_artikel(request, id):
    template_name = 'add_artikel.html'
    kategori = Kategori.objects.all()
    get_daftar = Daftar.objects.get(id=id)
    
    if request.method == "POST":
        forms_daftar = DaftarForms(request.POST, instance=get_daftar)
        if forms_daftar.is_valid():
           art = forms_daftar.save(commit=False)
           art.nama = request.user
           art.save()
        
        return redirect(list_artikel)
    else:
         forms_daftar = DaftarForms(instance=get_daftar)
    context = {
        'title' : 'Update Artikel',
        'kategori' : kategori,
        'get_daftar' : get_daftar,
        'forms_daftar' : forms_daftar

    }
    return render(request, template_name, context)

@login_required
def detail_artikel(request, id):
    template_name = "detail_artikel.html"
    artikel = Daftar.objects.get(id=id)
    context = {
        'title' : 'Detail Artikel',
        'artikel' : artikel,
    }
    return render(request, template_name, context)

@login_required
def delete_artikel(request, id):
    artikel = Daftar.objects.get(id=id).delete()
    return redirect(list_artikel)

