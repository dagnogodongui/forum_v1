from django.db import models
from base.models.helpers.name_datetime_model import NameDateTimeModel


class ForumModel(NameDateTimeModel):
    description = models.TextField()
    
    def __str__(self):
        return self.name
