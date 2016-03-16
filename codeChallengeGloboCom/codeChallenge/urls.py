from django.conf.urls import url
from django.views.generic import TemplateView
from codeChallenge.views import VoteView, LoginView
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^votar$', VoteView.as_view(template_name='result.html', participant_id='1'), name='votar'),
    url(r'^reports$', TemplateView.as_view(template_name='reports_login.html'), name='reports'),
    url(r'^logar$', LoginView.as_view(template_name='reports_login.html'), name='logar'),
]