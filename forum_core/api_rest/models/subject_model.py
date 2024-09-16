from django.db import models
from base.models.helpers.name_datetime_model import NameDateTimeModel
from .forum_model import ForumModel

class SubjectModel(NameDateTimeModel):
    forum = models.ForeignKey(ForumModel, on_delete=models.CASCADE,null=True)
    