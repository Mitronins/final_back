from django.contrib import admin


# Register your models here.
from app.models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
       'id', 'test', 'type', 'text')
    fields = (
       'test', 'type', 'text')
    # list_filter = ('order', 'cost')
    # inlines = (AdvantegesInline, UsersInline)


admin.site.register(Question, QuestionAdmin)
