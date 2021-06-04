from django.shortcuts import render, redirect
from .models import List


def index(request):
    lists = List.objects.all()
    return render(request, 'index.html', {'lists': lists})


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        list_obj = List.objects.create(title=title)
        return redirect('index')
    return render(request, 'index.html')


def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        list_obj = List.objects.get(id=id)
        list_obj.title = title
        list_obj.save()
        return redirect('index')
    return render(request, 'update.html')


def delete(request, id):
    if request.method == 'POST':
        list_obj = List.objects.get(id=id)
        list_obj.delete()
        return redirect('index')
    return render(request, 'index.html')
