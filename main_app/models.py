from django.db import models

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


class App(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    built = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Technologie(models.Model):
    tech = models.CharField(
        max_length=4, 
        choices=TECHNOLOGIES,
        default=TECHNOLOGIES[0][0]
    )
    
    app = models.ForeignKey(App, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_tech_display()}"