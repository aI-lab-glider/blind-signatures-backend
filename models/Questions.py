from django.db import models as m
from Polls import Polls


class Questions(m.Model):
    poll_id = m.ForeignKey(to=Polls,
                           on_delete=m.SET_NULL,
                           to_field='id',
                           null=False)
    question_text = m.CharField(max_length=255)
    answer_set = m.CharField(max_length=255)
    answer_count = m.CharField(max_length=255)
