from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

# Create your views here.
def homeview(request):
    return render(request, 'app1/home.html', {})

def formview(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/form.html', {'form': form})

def showview(request):
    obj = Movie.objects.all()
    return render(request, 'app1/show.html', {'obj': obj})

def updateview(request, pk):
    obj = Movie.objects.get(id = pk)
    form = MovieForm(instance=obj)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/form.html', {'form': form})

def deleteview(request, x):
    obj = Movie.objects.get(id=x)
    if request.method == 'POST':
        obj.delete()
        return redirect('/a1/sv/')
    return render(request, 'app1/success.html', {'obj': obj})

