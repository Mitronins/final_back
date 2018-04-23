from django.contrib import admin

# Register your models here.
from app.models import Question, Lesson, Chapter, Test, Answer


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
        'id', 'title', 'text', 'lesson')
    fields = (
        'title', 'text', 'lesson')


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


admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Answer, AnswerAdmin)
