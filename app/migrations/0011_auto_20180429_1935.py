# Generated by Django 2.0.4 on 2018-04-29 19:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_auto_20180429_1833'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDictionary',
            new_name='DictionaryUser',
        ),
        migrations.RenameModel(
            old_name='UserLesson',
            new_name='LessonUser',
        ),
    ]
