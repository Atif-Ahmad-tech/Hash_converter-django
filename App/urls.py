from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'home'),
    path('sha256/', views.Hash256, name = "sha256"),
    path('sha224/', views.Hash224, name = "sha224"),
    path('sha384/', views.Hash384, name = "sha384"),
    path('sha512/', views.Hash512, name = "sha512"),
    path('sha1/', views.Hash1, name = "sha1"),
    path('md5/', views.HashMd5, name = "md5"),
    path('md4/', views.HashMd4, name = "md4"),
]