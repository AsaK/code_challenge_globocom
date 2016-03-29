from django.views.generic import TemplateView
from contest.models import Contest
from participant.models import Participant
from django.utils import timezone
# Create your views here.


class ContestsView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(ContestsView, self).get_context_data(**kwargs)
        context['contests'] = Contest.objects.all()
        return context


class VotingView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(VotingView, self).get_context_data(**kwargs)
        context['participants'] = Participant.get_participants_contest(self.kwargs['pk'])
        context['contest'] = self.kwargs['pk']
        return context


class VoteView(VotingView):

    def get_context_data(self, **kwargs):
        self.vote(self.kwargs['pk'], self.kwargs['participant'])
        context = super(VoteView, self).get_context_data(**kwargs)
        return context

    def vote(self, contest, participant):
        brother = Participant.objects.get(pk=participant)
        paredao = Contest.objects.get(pk=contest)
        brother.vote_set.create(contest=paredao, vote_date=timezone.now())
        brother.save()


