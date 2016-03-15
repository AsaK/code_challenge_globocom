from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from codeChallenge.models import Participant, Vote
import datetime, math
# Create your views here.


class VoteView(TemplateView):
    template_name = ''
    participant_id = ''
    participant = None

    def get_context_data(self, **kwargs):
        context = super(VoteView, self).get_context_data(**kwargs)
        context['participant'] = self.participant
        context['votosParticipantes'] = self.votosParticipantesPercent()
        context['totalVotos'] = self.totalVotos()
        return context

    def post(self, request):
        postData = request.POST['participanteId']
        try:
            self.participant = Participant.objects.get(pk=postData)
            self.participant.vote_set.create(vote_date=datetime.datetime.now())
            self.participant.save()
        except Participant.DoesNotExist:
            self.participant = None
        if self.participant is not None:
            return super(TemplateView, self).render_to_response(self.get_context_data())
        else:
            return render(request, 'index.html')

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def votosParticipantesPercent(self):
        votosParticipantes = []
        for Participante in Participant.objects.all():
            votePercent = math.trunc((Participante.vote_set.count() / Vote.objects.count()) * 100)
            votosParticipantes.append(votePercent)
        return votosParticipantes

    def totalVotos(self):
        return Vote.objects.count()