from django.db import models
from django.db.models import Model

TYPES = (
    (0, 'Выбор ответа'),
    (1, 'Тестовое поле'),
)


class Test(Model):
    title = models.CharField(max_length=255, verbose_name='Название теста')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Question(Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPES, verbose_name='Тип вопроса', default=1)
    text = models.CharField(max_length=255, verbose_name='Текст вопроса')

    def __str__(self):
        return '{} - {}'.format(self.test, self.text[0:10])


class Answer(Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name='Текст ответа')
    is_true = models.BooleanField(verbose_name='Правильный ответ')

    def __str__(self):
        return self.text


class Lesson(Model):
    title = models.CharField(max_length=255, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Chapter(Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название главы')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title
