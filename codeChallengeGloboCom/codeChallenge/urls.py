from django.conf.urls import url
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from codeChallenge.models import Contest, Participant
from codeChallenge.views import VoteView, LoginView
from django.core.urlresolvers import reverse_lazy
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

    url(r'^votar$', VoteView.as_view(template_name='result.html', participant_id='1'), name='votar'),

    url(r'^reports$', TemplateView.as_view(template_name='reports_login.html'), name='reports'),

    url(r'^logar$', LoginView.as_view(template_name='reports_login.html'), name='logar'),

    url(r'^contest$', ListView.as_view(model=Contest, paginate_by=10), name='contest_list'),

    url(r'^contest/pagina/(?P<page>[0-9]+)/$', ListView.as_view(model=Contest, paginate_by=10), name='contest_list'),

    url(r'^contest/new$', CreateView.as_view(model=Contest, success_url=reverse_lazy('contest_list'),
                                             fields=['desc', 'end_date']), name='contest_new'),

    url(r'^contest/edit/(?P<pk>\d+)$', UpdateView.as_view(model=Contest, success_url=reverse_lazy('contest_list'),
                                                          fields=['desc', 'end_date']), name='contest_edit'),

    url(r'^contest/delete/(?P<pk>\d+)$', DeleteView.as_view(model=Contest, success_url=reverse_lazy('contest_list')),
                                                            name='contest_delete'),

    url(r'^participant$', ListView.as_view(model=Participant, paginate_by=10), name='participant_list'),

    url(r'^participant/pagina/(?P<page>[0-9]+)/$', ListView.as_view(model=Participant, paginate_by=10), name='participant_list'),

    url(r'^participant/new$', CreateView.as_view(model=Participant, success_url=reverse_lazy('participant_list'),
                                                 fields=['name', 'contest']), name='participant_new'),

    url(r'^participant/edit/(?P<pk>\d+)$', UpdateView.as_view(model=Participant, success_url=reverse_lazy('participant_list'),
                                                              fields=['name', 'contest']), name='participant_edit'),

    url(r'^participant/delete/(?P<pk>\d+)$', DeleteView.as_view(model=Participant,
                                                                success_url=reverse_lazy('participant_list')),name='participant_delete'),
]