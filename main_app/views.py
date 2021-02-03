from django.shortcuts import render, redirect
from .models import App, Technologie
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def apps_index(request):
    apps = App.objects.all()
    return render(request, 'apps/index.html', {'apps': apps})

def apps_detail(request, app_id):
    app = App.objects.get(id=app_id)
    return render(request, 'apps/detail.html', {'app': app})


class AppCreate(CreateView):
    model = App
    fields = ['name', 'description']

class AppUpdate(UpdateView):
    model = App
    fields = '__all__'

class AppDelete(DeleteView):
    model = App
    succes_url = '/apps/'

class TechnologieList(ListView):
    model = Technologie

class TechnologieDetail(DetailView):
    model = Technologie

class TechnologieCreate(CreateView):
    model = Technologie
    fields = '__all__'

class TechnologieDelete(DeleteView):
    model = Technologie
    success_url = '/technologies/'