import datetime

from django.http import HttpResponse
from models.User import User
from models.Polls import Polls
from models.Questions import Questions
from models.InternalID import Internal_IDs


def test_endpoint(request):
    user = User()
    user.email = 'test@email.com'
    user.password = '1'
    user.public_key = '12343252'
    user.save()

    polls = Polls()
    polls.title = 'Smth'
    polls.category = 'Cat'
    polls.description = 'Desc'
    polls.expiration_date = datetime.date(2021, 12, 1)
    polls.save()

    q = Questions()
    q.poll = polls
    q.question_text = 'Text'
    q.answer_count = '[12]; [123]; [32]'
    q.answer_set = '[A]; [B]; [C]'
    q.save()

    iid = Internal_IDs()
    iid.poll_id = polls.id
    iid.save()

    return HttpResponse("Test")
