# Generated by Django 3.0.8 on 2020-08-14 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0006_auto_20200814_0947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizzes',
            old_name='published',
            new_name='is_publ',
        ),
        migrations.RenameField(
            model_name='quizzes',
            old_name='published_datetime',
            new_name='publ_d_time',
        ),
        migrations.RenameField(
            model_name='quizzes',
            old_name='person',
            new_name='q_person',
        ),
    ]
