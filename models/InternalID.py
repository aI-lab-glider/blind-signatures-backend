from django.db import models as m
from .Polls import Polls


class Internal_IDs(m.Model):
    poll = m.ForeignKey(to=Polls,
                           on_delete=m.CASCADE,
                           to_field='id',
                           null=False)
