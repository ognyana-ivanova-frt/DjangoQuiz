from django.contrib import admin
from models import Answer, Question


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', )
    list_filter = ['question']
    search_fields = ['question']
    fieldsets = [
        (None,               {'fields': ['question']}),
    ]
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'question', 'correct']
    ordering = ['answer']

admin.site.register(Answer, AnswerAdmin)
