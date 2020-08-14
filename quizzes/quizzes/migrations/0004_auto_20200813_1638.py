# Generated by Django 3.0.8 on 2020-08-13 13:38

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_auto_20200812_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='static/media/quizzes/'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='static/media/quizzes/'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='quizzes',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='static/media/quizzes/'), upload_to=''),
        ),
    ]
