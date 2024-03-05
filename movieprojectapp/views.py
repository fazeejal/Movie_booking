from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movie  # Assuming that the models file is in the same directory as the views file
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm

# Create your views here.
def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        image=request.FILES['image']
        is_coming_soon = request.POST.get('is_coming_soon')
        is_running = request.POST.get('is_running')
        is_international_release = request.POST.get('is_international_release')
        is_coming_soon = is_coming_soon == 'on'
        is_running = is_running == 'on'
        is_international_release = is_international_release == 'on'


        a = Movie(name=name, desc=desc, year=year, image=image,is_coming_soon=is_coming_soon,is_running=is_running,is_international_release=is_international_release)
        a.save()
        return redirect('index')  # Redirect to the index page after successful submission

    return render(request, 'add.html')




def index(request):
    # Filter movies for each category
    coming_soon_movies = Movie.objects.filter(is_running=False, is_international_release=False)
    running_movies = Movie.objects.filter(is_running=True)
    international_movies = Movie.objects.filter(is_international_release=True)

    context = {
        'coming_soon_movies': coming_soon_movies,
        'running_movies': running_movies,
        'international_movies': international_movies,
    }
    return render(request, 'index.html', context)



def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie})

 
def delete(request,id):
    if request.method == "POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")

from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm



def update(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            # Redirect to the movie detail view with the updated movie_id
            return redirect('/', movie_id=movie.id)
    else:
        form = MovieForm(instance=movie)

    return render(request, 'update.html', {'form': form, 'movie': movie})
