# Generated by Django 3.0.8 on 2020-08-14 06:04

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercards', '0005_auto_20200813_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercard',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media/users/'), upload_to=''),
        ),
    ]