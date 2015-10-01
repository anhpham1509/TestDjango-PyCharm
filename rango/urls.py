from django.conf.urls import url
from rango import views

__author__ = 'DuyAnhPham'

urlpatterns = [
    url(r'^', views.index, name='index'), #in
]

