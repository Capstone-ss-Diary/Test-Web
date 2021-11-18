from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ocr_upload', views.ocr_upload, name='ocr_upload'),
]
