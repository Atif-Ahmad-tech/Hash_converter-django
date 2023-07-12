from django.shortcuts import render
from .models import Hashing
from .extras import *
    
def index(request):
    return render(request, 'index.html',)

def Hash256(request):
    media=Hashing.objects.get(hash_name='Sha256')
    if request.method=='POST':
        text = request.POST.get('text')
        print(text)
        hash_gen = sha_256(text)
        print(hash_gen)
        return render(request, 'sha256.html', context={'hash': hash_gen,'media': media})
    return render(request, 'sha256.html', context={'hash':'','media': media})

def Hash1(request):
    media=Hashing.objects.get(hash_name='Sha1')
    if request.method=='POST':
        text = request.POST.get('text')
        print(text)
        hash_gen = sha_1(text)
        print(hash_gen)
        return render(request, 'sha1.html', context={'hash': hash_gen,'media': media})
    return render(request, 'sha1.html', context={'hash':'','media': media})

def HashMd5(request):
    media=Hashing.objects.get(hash_name='Md5')
    if request.method=='POST':
        text = request.POST.get('text')
        print(text)
        hash_gen = md_5(text)
        print(hash_gen)
        return render(request, 'sha1.html', context={'hash': hash_gen,'media': media})
    return render(request, 'sha1.html', context={'hash':'','media': media})

