from django.db import models

# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    built = models.BooleanField(default=False)

    def __str__(self):
        return self.name