# Generated by Django 5.0.1 on 2024-01-23 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0003_initial'),
        ('User', '0017_delete_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=100)),
                ('complaint_description', models.CharField(max_length=500)),
                ('complaint_status', models.IntegerField(default=0)),
                ('complaint_date', models.DateField()),
                ('complaint_reply', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_newuser')),
            ],
        ),
    ]
