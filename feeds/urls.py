from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.detail, name='index'),
    # path('', views.about, name='index'),

]
