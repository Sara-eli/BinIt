from django.db import models
from Worker.models import *
from User.models import *
from Panchayath.models import *


# Create your models here.

class tbl_request(models.Model):
    user_wastetype=models.CharField(max_length=100)
    requset_date=models.DateField()
    request_amount=models.IntegerField()
    request_status=models.IntegerField(default=0)
    request_fordate=models.DateField()
    payment_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
    worker=models.ForeignKey(tbl_workerregistration,on_delete=models.CASCADE)

