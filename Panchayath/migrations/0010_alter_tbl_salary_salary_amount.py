# Generated by Django 5.0.1 on 2024-01-22 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Panchayath', '0009_tbl_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_salary',
            name='salary_amount',
            field=models.IntegerField(),
        ),
    ]
