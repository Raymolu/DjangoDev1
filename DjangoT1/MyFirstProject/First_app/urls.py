from django.conf.urls import url
from First_app import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('First_app/help/', views.help, name='help'),
]