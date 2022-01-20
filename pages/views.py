from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('<h1>Hello From Pages App</h1>')
    return render(request,'pages/index.html')#templates zaten belli olduğu için direkt içerisindeki dizini veriyoruz


def about(request):
    return render(request,'pages/about.html')#templates zaten belli olduğu için direkt içerisindeki dizini veriyoruz



