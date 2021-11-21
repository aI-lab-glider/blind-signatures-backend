from django.db import models as m

from models import Polls


class InternalID(m.Model):
    id = m.IntegerField()
    poll_id = m.ForeignKey(to=Polls,
                           on_delete=m.SET_NULL,
                           to_field=id,
                           null=False)
