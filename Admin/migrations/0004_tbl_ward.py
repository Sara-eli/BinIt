# Generated by Django 5.0 on 2023-12-30 04:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_tbl_panchayath_alter_tbl_admin_admin_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_number', models.IntegerField()),
                ('panchayath', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_panchayath')),
            ],
        ),
    ]
