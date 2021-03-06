# Generated by Django 2.0.4 on 2018-04-29 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название главы')),
                ('text', models.TextField(verbose_name='Текст')),
                ('queue', models.IntegerField(default=1, verbose_name='Очередь в уроке')),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Мой словарь', max_length=255, verbose_name='Название')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название урока')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='LessonUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'В процессе'), (1, 'Закончен')], default=0, verbose_name='Статус теста')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'Выбор ответа'), (1, 'Тестовое поле')], default=1, verbose_name='Тип вопроса')),
                ('text', models.CharField(max_length=255, verbose_name='Текст вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название теста')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='TestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'В процессе'), (1, 'Закончен')], default=0, verbose_name='Статус теста')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Test')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_word', models.CharField(max_length=255, verbose_name='Слово на английском')),
                ('ru_word', models.CharField(max_length=255, verbose_name='Слово на русском')),
                ('note', models.TextField(verbose_name='Заметка')),
                ('dictionary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Dictionary')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Test'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Lesson'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='testuser',
            unique_together={('test', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='lessonuser',
            unique_together={('lesson', 'user')},
        ),
    ]
