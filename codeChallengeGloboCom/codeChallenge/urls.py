from django.conf.urls import url
from django.views.generic import TemplateView
from codeChallenge.views import VoteView
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^votar$', VoteView.as_view(template_name='index.html', participant_id='1'), name='votar'),
]