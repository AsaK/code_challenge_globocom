from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, FormView
from codeChallenge.models import Participant, Vote
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
import datetime, math
# Create your views here.


class LoginView(FormView):
    template_name = 'reports_login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('reports')

    def form_valid(self, form):
        username = form['username']
        password = form['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return super(LoginView, self).form_valid(form)
            else:
                messages.error(self.request, 'Não foi possível autenticar as credênciais')
                render(self.request, 'reports_login.html')
                

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