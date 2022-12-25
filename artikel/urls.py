from django.urls import path, include
from artikel.views import *
# from . import views

urlpatterns = [
    path('list', list_artikel, name='list_artikel'),
    path('add', add_artikel, name='add_artikel'),
    path('users/', users, name='users'),
    path('detail/<int:id>', detail_artikel, name='detail_artikel'),
    path('update/<int:id>', update_artikel, name='update_artikel'),
    path('delete/<int:id>', delete_artikel, name='delete_artikel'),
]
