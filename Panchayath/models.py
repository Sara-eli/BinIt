from django.db import models
from  Admin.models import *

# Create your models here.

class tbl_workerregistration(models.Model):
    worker_name=models.CharField(max_length=20)
    worker_contact=models.CharField(max_length=10)
    worker_password=models.CharField(max_length=20)
    worker_email=models.EmailField()
    worker_gender=models.CharField(max_length=10)
    worker_salary=models.CharField(max_length=15,null=True)
    worker_proof=models.FileField(upload_to='UserDocs/')
    worker_photo=models.FileField(upload_to='UserDocs/')
    worker_status=models.IntegerField(default=0)
    ward_id=models.ForeignKey(tbl_ward,on_delete=models.CASCADE,null=True)


class tbl_salary(models.Model):
    salary_date=models.DateField()
    salary_amount=models.IntegerField()
    salary_status=models.IntegerField(default=0)
    worker=models.ForeignKey(tbl_workerregistration,on_delete=models.CASCADE)

class tbl_assing(models.Model):
    worker = models.ForeignKey(tbl_workerregistration,on_delete=models.CASCADE)
    ward = models.ForeignKey(tbl_ward,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)