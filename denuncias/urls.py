from django.urls import path
from .views import list_denuncias, create_denuncias, update_denuncias, delete_denuncias

urlpatterns = [
    path('',list_denuncias, name='list_denuncias'),
    path('new', create_denuncias, name='create_denuncias'),
    path('update/<int:id>/', update_denuncias, name='update_denuncias'),
    path('delete/<int:id>/', delete_denuncias, name='delete_denuncias'),
]

