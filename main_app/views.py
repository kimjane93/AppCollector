from django.shortcuts import render, redirect
from .models import App, Technologie, Note
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def apps_index(request):
    # apps = App.objects.all()
    apps = App.objects.filter(user=request.user)
    return render(request, 'apps/index.html', {'apps': apps})

@login_required
def apps_detail(request, app_id):
    app = App.objects.get(id=app_id)
    note_form = NoteForm()
    technologies_app_doesnt_have = Technologie.objects.exclude(id__in = app.tech.all().values_list('id'))
    return render(request, 'apps/detail.html', {
    'app': app, 'technologies': technologies_app_doesnt_have,
    'note_form': note_form
    })
    return render(request, 'apps/detail.html', {'app': app, 'note_form': note_form})

@login_required
def assoc_technologie(request, app_id, technologie_id):
    App.objects.get(id=app_id).tech.add(technologie_id)
    return redirect('detail', app_id=app_id)

@login_required
def add_note(request, app_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.app_id = app_id
        new_note.save()
    return redirect('detail', app_id=app_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
        form = UserCreationForm(request.POST)
    if form.is_valid():
        # This will add the user to the database
        user = form.save()
        # This is how we log a user in via code
        login(request, user)
        return redirect('index')
    else:
        error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context) 

class AppCreate(LoginRequiredMixin, CreateView):
    model = App
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AppUpdate(LoginRequiredMixin, UpdateView):
    model = App
    fields = ['name', 'description', 'built']

class AppDelete(LoginRequiredMixin, DeleteView):
    model = App
    succes_url = '/apps/'

class TechnologieList(LoginRequiredMixin, ListView):
    model = Technologie

class TechnologieDetail(LoginRequiredMixin, DetailView):
    model = Technologie

class TechnologieCreate(LoginRequiredMixin, CreateView):
    model = Technologie
    fields = '__all__'

class TechnologieDelete(LoginRequiredMixin, DeleteView):
    model = Technologie
    success_url = '/technologies/'