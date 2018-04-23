# Generated by Django 2.0.4 on 2018-04-22 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Текст ответа')),
                ('is_true', models.BooleanField(verbose_name='Правильный ответ')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.IntegerField(choices=[(0, 'Выбор ответа'), (1, 'Тестовое поле')], default=1, verbose_name='Тип вопроса'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question'),
        ),
    ]