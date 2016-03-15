from django.db import models
import datetime

# Create your models here.


class Contest(models.Model):
    end_date = models.DateTimeField()


class Participant(models.Model):
    name = models.TextField(max_length=100)
    contest = models.ForeignKey(Contest)


class Vote(models.Model):
    participant = models.ForeignKey(Participant)
    vote_date = models.DateTimeField()
