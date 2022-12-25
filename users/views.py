from django.shortcuts import render, redirect
from users.models import *
from .forms import BiodataForms
from django.contrib.auth.models import User
# Create your views here.


def is_operator(user):
    if user.groups.filter(name='operator').exists():
        
        return True
    else:
        return False

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

def users(request):
    template_name = 'users.html'
    biodata = User.objects.all()
    context = {
        'title' : 'Halaman Biodata',
        'biodata' : biodata
    }

    return render(request, template_name, context)

def detail_biodata(request, id):
    template_name = "detail_biodata.html"
    list_biodata = User.objects.get(id=id)
    context = {
        'title' : 'Detail Biodata',
        'list_biodata' : list_biodata,
    }
    return render(request, template_name, context)

def update_biodata(request, id):
    template_name = 'register.html'
    get_biodata = User.objects.get(id=id)
    
    if request.method == "POST":
        form_biodata = BiodataForms(request.POST, instance=get_biodata)
        if form_biodata.is_valid():
           art = form_biodata.save(commit=False)
           art.user = request.user
           art.save()
        
        return redirect(users)
    else:
         form_biodata = BiodataForms(instance=get_biodata)
    context = {
        'title' : 'Update Biodata',
        # 'kategori' : kategori,
        'get_daftar' : get_biodata,
        'from_biodata' : form_biodata

    }
    return render(request, template_name, context)

def delete_biodata(request, id):
    biodata = User.objects.get(id=id).delete()
    return redirect(users)
