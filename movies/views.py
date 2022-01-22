from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Movie
# Create your views here.

def index(request):
    # movie içerisinde üretilen tüm objeleri çağırır.
    movies = Movie.objects.all()
    context={
        'movies': movies
    
        # list html sayfasının en üstünde adımı yazdırdım.
        # 'name':'Fatma Zehra Yılmaz'
    }

    return render(request,'movies/list.html',context)

def detail(request, movie_id):
## Sayfa bulunamazsa hata mesajı bu şekilde oluşturulabilir yada shortcut kullanılır.

    # try:
    #     movie=Movie.objects.get(pk=movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404('Aradığınız kayıt bulunamadı')

## Shortcut hali 
    movie=get_object_or_404(Movie, pk=movie_id )

    context={
        'movie' : movie 
    }

    return render(request,'movies/detail.html',context)

def search(request):
    return render(request,'movies/search.html')

