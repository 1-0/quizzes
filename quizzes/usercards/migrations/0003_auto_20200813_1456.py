# Generated by Django 3.0.8 on 2020-08-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercards', '0002_auto_20200810_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercard',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/users/'),
        ),
    ]
