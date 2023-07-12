from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'home'),
    path('sha256/', views.Hash256, name = "sha256"),
    path('sha1/', views.Hash1, name = "sha1"),
    path('md5/', views.HashMd5, name = "md5"),
]