from django.conf.urls import url
from poll.views import ContestsView, VotingView, VoteView
urlpatterns = [
    url(r'^$', ContestsView.as_view(template_name='index.html'), name='index'),
    url(r'^poll/(?P<pk>\d+)$', VotingView.as_view(template_name='voting.html'), name='votacao'),
    url(r'^poll/(?P<pk>\d+)/participant/(?P<participant>\d+)$', VoteView.as_view(template_name='voting.html'), name='votar'),
]
