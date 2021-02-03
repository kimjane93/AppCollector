from django.db import models
from django.urls import reverse

# Create your models here.
TECHNOLOGIES  = (
    ('JS', 'Javascript'),
    ('PY', 'Python'),
    ('HTML', 'Hyper Text Reference Language'),
    ('CSS', 'Cascading Style Sheets'),
    ('RCT', 'React Framework'),
    ('DJO', 'Django Framework'),
    ('PSQL', 'PostgreSQL DB'),
    ('MGO', 'Mongo No-SQL DB'),
    ('OAUT', 'O-authentication'),
    ('JWT', 'Json Web Tokens'),
    ('MTZ', 'Materialize Library'),
    ('BTSP', 'Boostrap Library'),
    ('SMTC', 'Semantic UI Library'),
    ('NODE', 'Node.js Runtime Environment'),
    ('SRG', 'Surge.sh Deployment Platform'),
    ('HRKU', 'Heroku Deploymeny Platform'),
    ('PTMN', 'Postman')
)

BUILD_STATUS = (
    ('B', 'Built'),
    ('NB', 'Not Built')
)

class Technologie(models.Model):
    name = models.CharField(
        # max_length=4, 
        # choices=TECHNOLOGIES,
        # default=TECHNOLOGIES[0][0]
        max_length=50, 
        default=''
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('technologies_detail', kwargs={'pk': self.id})

class App(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    built = models.CharField(
        max_length=2, 
        choices=BUILD_STATUS,
        default=BUILD_STATUS[1][0]
    )
    tech = models.ManyToManyField(Technologie)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'app_id': self.id})


