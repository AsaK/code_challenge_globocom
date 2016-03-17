from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Contest(models.Model):
    name = models.TextField(verbose_name=u'Nome da votação', max_length=255, blank=False, null=False)
    desc = models.TextField(verbose_name=u'Descrição da votação', max_length=255, blank=False, null=False)
    start_date = models.DateTimeField(verbose_name=u'Data inicial', null=False, blank=False)
    end_date = models.DateTimeField(verbose_name=u'Data final', null=False, blank=False)
    logo = models.ImageField(verbose_name=u'Logo da votação', null=True, blank=True, upload_to='Logos')

    def __str__(self):
        return self.name + ' ' + self.desc

    def get_absolute_url(self):
        return reverse('contest_edit', kwargs={'pk': self.pk})
