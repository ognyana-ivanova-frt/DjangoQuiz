from django import forms
from dbsettings import values
from django.db import models
import dbsettings


class MinAnswersValue(values.IntegerValue):

    class field(forms.IntegerField):

        def __init__(self, *args, **kwargs):
            kwargs['min_value'] = 2

            max_count_answers = []
            questions = Question.objects.all()
            for question in questions:
                answers = question.answer_set.all()
                max_count_answers.append(int(len(answers)))

            kwargs['max_value'] = int(min(max_count_answers))
            forms.IntegerField.__init__(self, *args, **kwargs)


class MaxQuestionsValue(values.IntegerValue):

    class field(forms.IntegerField):

        def __init__(self, *args, **kwargs):
            kwargs['min_value'] = 1
            kwargs['max_value'] = len(Question.objects.all())
            forms.IntegerField.__init__(self, *args, **kwargs)


class QuestionLimits(dbsettings.Group):
    count_questions = MaxQuestionsValue()


class AnswerLimits(dbsettings.Group):
    count_answers = MinAnswersValue()


class Question(models.Model):
    question = models.CharField(max_length=200)
    options = QuestionLimits()

    def get_count_questions(self):
        return Question.options.count_questions

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=60)
    question = models.ForeignKey(Question)
    correct = models.BooleanField(default=False)
    options = AnswerLimits()

    def get_count_answers(self):
        return Answer.options.count_answers

    def __str__(self):
        return self.answer





