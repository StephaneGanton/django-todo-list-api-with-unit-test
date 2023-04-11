from django.db import models
from authentication.models import User

from helpers.models import TrackingModel


class Todo(TrackingModel):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_complete = models.BooleanField( default = False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    # get a string representation of the class

    def __str__(self):
        return self.title
