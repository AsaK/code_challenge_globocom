from django.conf.urls import url
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from contest.models import Contest
from django.core.urlresolvers import reverse_lazy
urlpatterns = [
    url(r'^$', ListView.as_view(model=Contest, paginate_by=10), name='contest_list'),
    url(r'^pagina/(?P<page>[0-9]+)/$', ListView.as_view(model=Contest, paginate_by=10), name='contest_list'),
    url(r'^new$', CreateView.as_view(model=Contest, success_url=reverse_lazy('contest_list'),
                                     fields=['name', 'desc', 'logo', 'start_date', 'end_date']),
        name='contest_new'),

    url(r'^edit/(?P<pk>\d+)$', UpdateView.as_view(model=Contest, success_url=reverse_lazy('contest_list'),
                                                  fields=['name', 'desc', 'logo', 'start_date', 'end_date']),
        name='contest_edit'),

    url(r'^delete/(?P<pk>\d+)$', DeleteView.as_view(model=Contest, success_url=reverse_lazy('contest_list')),
                                                            name='contest_delete'),
]
