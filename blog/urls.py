from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pub, name='post_list'),
]
