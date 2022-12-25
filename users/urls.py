from django.urls import path, include
from users.views import *

urlpatterns = [
    path('list', users, name='users'),
    # path('add', add_artikel, name='add_artikel'),
    # path('users/', users, name='users'),
    path('detail/<int:id>', detail_biodata, name='detail_biodata'),
    path('update/<int:id>', update_biodata, name='update_biodata'),
    path('delete/<int:id>', delete_biodata, name='delete_biodata'),
]
