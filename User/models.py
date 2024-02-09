from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
#

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=100)
    complaint_description=models.CharField(max_length=500)
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
    complaint_status=models.IntegerField(default=0)
    complaint_date=models.DateField()
    complaint_reply=models.CharField(max_length=500)


class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=600)
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)