from django.contrib import admin

# Register your models here.
from app.models import Question, Lesson, Chapter, Test, Answer, Word, Dictionary


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'test', 'type', 'text')
    fields = (
        'test', 'type', 'text')
    # list_filter = ('order', 'cost')
    # inlines = (AdvantegesInline, UsersInline)


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description')
    fields = (
        'title', 'description')


class ChapterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'text', 'lesson', 'queue')
    fields = (
        'title', 'text', 'lesson', 'queue')


class TestAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description')
    fields = (
        'title', 'description')


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'question', 'text', 'is_true')
    fields = (
        'question', 'text', 'is_true')


class DictionaryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title')
    fields = ('title',)


class WordAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'en_word', 'ru_word', 'note')
    fields = (
        'en_word', 'ru_word', 'note', 'dictionary')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Dictionary, DictionaryAdmin)
