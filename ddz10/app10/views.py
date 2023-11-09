from django.shortcuts import render

from app10.models import Genre, Executor


# Create your views here.
def index(request):
    context = {'genres':Genre.objects.all()}
    return render(request, 'index.html', context=context)



def executor(request, genre):
    executor = Executor.objects.filter(genre__name=genre)
    context = {'executors': executor}
    return render(request, 'executors.html', context=context)



def detail(request,genre,slug):
    context ={'detail':Executor.objects.get(slug=slug)}
    return render(request, 'detail.html', context=context)