from django.forms import ModelForm
from .models import Technologie

class TechnologieForm(ModelForm):
    class Meta: 
        model = Technologie
        fields = ['tech']