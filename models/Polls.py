from django.db import models as m


class Polls(m.Model):
    title = m.CharField(max_length=255)
    category = m.CharField(max_length=255)
    description = m.CharField(max_length=255)
    expiration_date = m.DateTimeField()
