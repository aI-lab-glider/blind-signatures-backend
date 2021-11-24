from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from models.User import User

"""
{
    "email": "abc@mail.com",
    "password": "pass",
    "public_key": "123432525"
}
"""


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        user_data = json.loads(request.body)
        user = User()
        user.email = user_data['email']
        user.password = user_data['password']  # TODO: Make encoded password setter
        user.public_key = user_data['public_key']
        user.save()
        return HttpResponse('OK')
