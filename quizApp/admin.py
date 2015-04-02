from django.contrib import admin
from models import Answer, Question


class AnswerInline(admin.StackedInline):
    """
    Adding Answer objects
    """
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    """
    Customize the admin form
    """
    list_display = ('question', )
    list_filter = ['question']
    search_fields = ['question']
    fieldsets = [
        (None, {'fields': ['question']}),
    ]
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)  # registering the Question model


class AnswerAdmin(admin.ModelAdmin):
    """
    Customize the admin form
    """
    list_display = ['answer', 'question', 'correct']
    ordering = ['answer']

admin.site.register(Answer, AnswerAdmin)  # registering the Answer model
