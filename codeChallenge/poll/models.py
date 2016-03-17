from django.db import models
from participant.models import Participant
from contest.models import Contest
# Create your models here.


class Vote(models.Model):
    participant = models.ForeignKey(Participant)
    contest = models.ForeignKey(Contest)
    vote_date = models.DateTimeField()
