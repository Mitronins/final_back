from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model

TYPES = (
    (0, 'Выбор ответа'),
    (1, 'Тестовое поле'),
)

STATUS = (
    (0, 'В процессе'),
    (1, 'Закончен'),
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
    queue = models.IntegerField(verbose_name='Очередь в уроке', default=1)

    def __str__(self):
        return self.title


class Dictionary(Model):
    title = models.CharField(max_length=255, verbose_name='Название', default='Мой словарь')

    def __str__(self):
        return self.title


class Word(Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    en_word = models.CharField(max_length=255, verbose_name='Слово на английском')
    ru_word = models.CharField(max_length=255, verbose_name='Слово на русском')
    note = models.TextField(verbose_name='Заметка')


class DictionaryUser(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE)


class LessonUser(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, verbose_name='Статус теста', default=0)

    class Meta:
        unique_together = ('lesson', 'user')


class TestUser(Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    status = models.IntegerField(choices=STATUS, verbose_name='Статус теста', default=0)

    class Meta:
        unique_together = ('test', 'user')
