# Generated by Django 5.0.1 on 2024-01-22 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_complaint',
            name='ward',
        ),
    ]