# Generated by Django 5.0.1 on 2024-01-22 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_complaint',
        ),
    ]