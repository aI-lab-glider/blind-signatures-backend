from models.Polls import Polls
from models.Questions import Questions
from django.http import JsonResponse
from django.forms.models import model_to_dict


def polls(request):
    if request.method == 'GET':
        polls_list = list(Polls.objects.values())
        return JsonResponse(polls_list, safe=False)


def polls_by_id(request, id_arg):
    if request.method == 'GET':
        poll = Polls.objects.get(id=id_arg)
        return JsonResponse(model_to_dict(poll), safe=False)


def questions_by_id(request, id_arg):
    if request.method == 'GET':
        questions = Questions.objects.get(poll_id=id_arg)
        return JsonResponse(model_to_dict(questions), safe=False)


def verify(request):
    if request.method == 'POST':
        print(request)
        return JsonResponse({"success": True}, safe=False)
