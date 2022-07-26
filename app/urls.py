from django.conf.urls import url,include

from . import views

urlpatterns = [
    url('index', views.index, name='index'),
    url('readcsv', views.readcsv, name='readcsv'),
    url('endpoint1', views.endpoint1, name='endpoint1'),
    url('endpoint2', views.endpoint2, name='endpoint2'),  
]
