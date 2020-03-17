from django.conf.urls import url
from FirstFormApp import views
from django.urls import path, include

app_name = 'FirstFormApp'

urlpatterns = [
    path('', views.initial, name='initial'),
    path('help/', views.help, name='help'),
    path('form1/', views.form_name_view, name='form1'),
]