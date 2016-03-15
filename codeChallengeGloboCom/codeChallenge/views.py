from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from codeChallenge.models import Participant
import datetime
# Create your views here.


class VoteView(View):
    template_name = ''
    participant_id = ''

    def post(self, request):
        postData = request.POST['participanteId']
        try:
            participant = Participant.objects.get(pk=postData)
            participant.vote_set.create(vote_date=datetime.datetime.now())
            participant.save()
        except Participant.DoesNotExist:
            participant = None
        if participant is not None:
            return render(request, 'result.html', {'participant': participant})        
        else:
            return render(request, 'index.html')
    def get(self, request):
        return render(request, 'index.html')
