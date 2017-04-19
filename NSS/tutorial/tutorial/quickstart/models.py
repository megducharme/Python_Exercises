from django.db import models

class HockeyTeams(models.Model):
    teamname = models.CharField(max_length=44)
    logo = models.FilePathField(path="/static/logos")
    city = models.CharField(max_length=255)
    coach = models.CharField(max_length=55)
    mascot = models.CharField(max_length=55)

    def __str__():
        return self.teamname


class HockeyPlayer(models.Model):
    playername = models.CharField(max_length=55)
    team = models.ForeignKey(HockeyTeams)
    position = models.CharField(max_length=22)


class Cohort(models.Model):
    name = models.CharField(max_length=44)

