from django.db import models
from django.core.urlresolvers import reverse
from contest.models import Contest


class Participant(models.Model):
    name = models.TextField(verbose_name=u'Nome', max_length=100)
    desc = models.TextField(verbose_name=u'Descrição de votação', blank=True, null=True)
    contest = models.ManyToManyField(Contest, verbose_name=u'Paredão')
    picture = models.ImageField(verbose_name=u'Foto', null=False, blank=False, upload_to='Pictures')
    active = models.BooleanField(verbose_name=u'Eliminado', default=False)

    def __str__(self):
        return self.name

    def get_abosulte_url(self):
        return reverse('participant_edit', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('name',)
