from django.shortcuts import render, redirect
from .models import App, Technologie, Note
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import NoteForm

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
    note_form = NoteForm()
    technologies_app_doesnt_have = Technologie.objects.exclude(id__in = app.tech.all().values_list('id'))
    return render(request, 'apps/detail.html', {
    'app': app, 'technologies': technologies_app_doesnt_have,
    'note_form': note_form
    })
    return render(request, 'apps/detail.html', {'app': app, 'note_form': note_form})

def assoc_technologie(request, app_id, technologie_id):
    App.objects.get(id=app_id).tech.add(technologie_id)
    return redirect('detail', app_id=app_id)

def add_note(request, app_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.app_id = app_id
        new_note.save()
    return redirect('detail', app_id=app_id)

class AppCreate(CreateView):
    model = App
    fields = ['name', 'description']

class AppUpdate(UpdateView):
    model = App
    fields = ['name', 'description', 'built']

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