# Generated by Django 5.0 on 2023-12-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_waste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_type', models.CharField(max_length=20)),
            ],
        ),
    ]