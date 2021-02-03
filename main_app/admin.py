from django.contrib import admin
from .models import App, Technologie, Note

# Register your models here.
admin.site.register(App)
admin.site.register(Technologie)
admin.site.register(Note)