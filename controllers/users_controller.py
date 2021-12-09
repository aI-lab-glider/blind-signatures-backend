import json

import models
from models.User import User
from django.http import JsonResponse
from django.forms.models import model_to_dict


def login(request):
    if request.method == 'POST':
        print(request.body)
        json_data = json.loads(request.body)
        email = json_data['user']['email']
        password = json_data['user']['password']
        user = User.objects.get(email=email, password=password)
        data = model_to_dict(user)
        data.pop('password')
        return JsonResponse(data, safe=False)

def register(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        user = User()
        user.email = json_data['user']['email']
        user.password = json_data['user']['password']
        user.public_key = json_data['user']['public_key']
        try:
            existing_user = User.objects.get(email=user.email)
            raise ValueError("User already exists.")
        except models.User.User.DoesNotExist as e:
            print(len(user.public_key))
            user.save()
            data = model_to_dict(user)
            data.pop('password')
            return JsonResponse(data, safe=False)

def delete(request):
    if request.method == 'DELETE':
        json_data = json.loads(request.body)
        user = User()
        user.email = json_data['user']['email']
        user.public_key = json_data['user']['public_key']
        User.objects.get(email=user.email, public_key=user.public_key).delete()
        return JsonResponse({"success": True}, safe=False)
