from django.db import models
from django.core.urlresolvers import reverse
import datetime

# Create your models here.


class Contest(models.Model):
    desc = models.TextField(verbose_name=u'Descrição', max_length=255, blank=False, null=False)
    end_date = models.DateTimeField(verbose_name=u'Data final', null=False, blank=False)

    def __str__(self):
        return self.desc

    def get_absolute_url(self):
        return reverse('contest_edit', kwargs={'pk': self.pk})


class Participant(models.Model):
    name = models.TextField(verbose_name=u'Nome', max_length=100)
    contest = models.ForeignKey(Contest, verbose_name=u'Paredão')
    picture = models.ImageField(verbose_name=u'Imagem', null=False, blank=False, upload_to='Pictures')

    def __str__(self):
        return self.name

    def get_abosulte_url(self):
        return reverse('participant_edit', kwargs={'pk': self.pk})


class Vote(models.Model):
    participant = models.ForeignKey(Participant)
    vote_date = models.DateTimeField(null=False, default=datetime.datetime.now())
