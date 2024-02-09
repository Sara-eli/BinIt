from django.db import models
from Admin.models import*

# Create your models here.

class tbl_newuser(models.Model):
    user_name=models.CharField(max_length=20)
    user_contact=models.CharField(max_length=20)
    user_password=models.CharField(max_length=20)
    user_proof=models.FileField(upload_to='UserDocs/')
    user_email=models.EmailField()
    user_address=models.CharField(max_length=20)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)

