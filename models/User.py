from django.db import models as m


class User(m.Model):
    email = m.EmailField()
    password = m.CharField(max_length=255)
    public_key = m.CharField(max_length=255)
