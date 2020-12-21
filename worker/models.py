from django.db import models
from authentication.models import User
from core.models import Field

class Worker(models.Model):
    worker = models.ForeignKey(User,on_delete=models.CASCADE)
    field =  models.ForeignKey(Field,on_delete=models.CASCADE)
    def __str__(self):
        return self.worker

class Activity(models.Model):
    STATES = (
      ('UPDATE', 'Update'),
      ('CUTDOWN', 'CutDown'),
      ('DISEASE', 'Disease'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    field =  models.ForeignKey(Field,on_delete=models.CASCADE)
    activity = models.CharField(choices=STATES,max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity