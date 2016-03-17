from django.conf.urls import url
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from participant.models import Participant
from django.core.urlresolvers import reverse_lazy
urlpatterns = [
    url(r'^$', ListView.as_view(model=Participant, paginate_by=10), name='participant_list'),
    url(r'^pagina/(?P<page>[0-9]+)/$', ListView.as_view(model=Participant, paginate_by=10), name='participant_list'),
    url(r'^new$', CreateView.as_view(model=Participant, success_url=reverse_lazy('participant_list'),
                                     fields=['name', 'desc','contest', 'picture', 'active']), name='participant_new'),
    url(r'^edit/(?P<pk>\d+)$', UpdateView.as_view(model=Participant, success_url=reverse_lazy('participant_list'),
                                                  fields=['name', 'desc', 'contest', 'picture', 'active']),
        name='participant_edit'),

    url(r'^delete/(?P<pk>\d+)$', DeleteView.as_view(model=Participant, success_url=reverse_lazy('participant_list')),
                                                    name='participant_delete'),
]
