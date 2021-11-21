from django.db import models as m
from .Polls import Polls


class Questions(m.Model):
    poll = m.ForeignKey(to=Polls,
                           on_delete=m.CASCADE,
                           to_field='id',
                           null=False)
    question_text = m.CharField(max_length=255)
    answer_set = m.CharField(max_length=255)
    answer_count = m.CharField(max_length=255)
