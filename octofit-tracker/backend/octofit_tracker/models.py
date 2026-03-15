from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'
