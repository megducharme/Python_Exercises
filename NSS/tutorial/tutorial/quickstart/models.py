from django.db import models

# Create your models here.
class HockeyTeams(models.Model):
    teamname = models.CharField(max_length=44)
    logo = models.FilePathField(path="/static/logos")
    city = models.CharField(max_length=255)
    coach = models.CharField(max_length=55)
    mascot = models.CharField(max_length=55)
