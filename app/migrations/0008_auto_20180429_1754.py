# Generated by Django 2.0.4 on 2018-04-29 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180429_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertest',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
