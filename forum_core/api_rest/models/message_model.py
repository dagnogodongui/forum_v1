from django.db import models
from base.models.helpers.name_datetime_model import NameDateTimeModel

class MessageModel(NameDateTimeModel):
    sujet = models.ForeignKey(SubjectModel, on_delete=models.set)
    