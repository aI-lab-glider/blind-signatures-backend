from django.http import HttpResponse
from models.User import User

def test_endpoint(request):
    user = User()
    user.email = 'test@email.com'
    user.password = '1'
    user.public_key = '12343252'
    user.save()
    return HttpResponse("Test")
