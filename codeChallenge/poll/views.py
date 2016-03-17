from django.shortcuts import render
from django.views.generic import TemplateView
from contest.models import Contest
from participant.models import Participant
import datetime
# Create your views here.


class ContestsView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(ContestsView, self).get_context_data(**kwargs)
        context['contests'] = Contest.objects.all()
        return context


class VotingView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(VotingView, self).get_context_data(**kwargs)
        context['participants'] = self.get_participants()
        context['contest'] = self.kwargs['pk']
        return context

    def get_participants(self):
        contest = Contest.objects.get(pk=self.kwargs['pk'])
        participants = contest.participant_set.all()
        return participants


class VoteView(VotingView):

    def get_context_data(self, **kwargs):
        self.vote(self.kwargs['pk'], self.kwargs['participant'])
        context = super(VoteView, self).get_context_data(**kwargs)
        return context

    def vote(self, contest, participant):
        brother = Participant.objects.get(pk=participant)
        paredao = Contest.objects.get(pk=contest)
        brother.vote_set.create(contest=paredao, vote_date=datetime.datetime.now())
        brother.save()


