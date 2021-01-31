from django.shortcuts import render, redirect
from .models import App
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TechnologieForm


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
    technologie_form = TechnologieForm()
    return render(request, 'apps/detail.html', {'app': app, 'technologie_form': technologie_form})

def add_technologie(request, app_id):
    form = TechnologieForm(request.POST)
     # validate the form
    if form.is_valid():
        # don't save form to the db until you manually ad teh cat id to it sinc ethere is no built in field for that
        new_technologie = form.save(commit=False)
        new_technologie.app_id = app_id
        new_technologie.save()
    return redirect('detail', app_id=app_id)

class AppCreate(CreateView):
    model = App
    fields = '__all__'

class AppUpdate(UpdateView):
    model = App
    fields = '__all__'

class AppDelete(DeleteView):
    model = App
    succes_url = '/apps/'