from django.db import models

#Create your models here.

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=20)
    admin_email=models.EmailField()
    admin_password=models.CharField(max_length=20)

class tbl_panchayath(models.Model):
    panchayath_name=models.CharField(max_length=20)
    panchayath_contact=models.IntegerField()
    panchayath_email=models.EmailField()
    panchayath_password=models.CharField(max_length=20)

class tbl_ward(models.Model):
    ward_number=models.IntegerField()
    panchayath=models.ForeignKey(tbl_panchayath,on_delete=models.CASCADE)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=20)
    ward=models.ForeignKey(tbl_ward,on_delete=models.CASCADE)

class tbl_waste(models.Model):
    waste_type=models.CharField(max_length=20)
    

