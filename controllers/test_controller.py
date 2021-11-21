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
    polls.save()

    q = Questions()
    q.poll = polls
    q.question_text = 'Text'
    q.answer_count = 'Count'
    q.answer_set = 'Set'
    q.save()

    iid = Internal_IDs()
    iid.poll_id = polls.id
    iid.save()

    return HttpResponse("Test")
