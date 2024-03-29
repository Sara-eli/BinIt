# Generated by Django 5.0.1 on 2024-01-24 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_tbl_waste'),
        ('Panchayath', '0010_alter_tbl_salary_salary_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_assing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_ward')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Panchayath.tbl_workerregistration')),
            ],
        ),
    ]
