from django import forms
from dbsettings import values
from django.db import models
import dbsettings


class MinAnswersValue(values.IntegerValue):
    """
    New Form field
    """

    class field(forms.IntegerField):
        """
        Returns a django.forms.Field instance for this database Field.
        """

        def __init__(self, *args, **kwargs):
            """
            Validates that the input is a integer number.
            Ensures that value of result is between [min_value, max_value]
            """
            kwargs['min_value'] = 2

            max_count_answers = []
            questions = Question.objects.all()  # getting all questions
            for question in questions:
                answers = question.answer_set.all()  # getting all answers for question
                max_count_answers.append(int(len(answers)))

            kwargs['max_value'] = int(min(max_count_answers))  # getting min length of answers for all questions
            forms.IntegerField.__init__(self, *args, **kwargs)


class MaxQuestionsValue(values.IntegerValue):
    """
    New Form field
    """

    class field(forms.IntegerField):
        """
        Returns a django.forms.Field instance for this database Field.
        """

        def __init__(self, *args, **kwargs):
            """
            Validates that the input is a integer number.
            Ensures that value of result is between [min_value, max_value]
            """
            kwargs['min_value'] = 1
            kwargs['max_value'] = len(Question.objects.all())
            forms.IntegerField.__init__(self, *args, **kwargs)


class QuestionLimits(dbsettings.Group):
    """
    Defining individual settings for questions
    """
    count_questions = MaxQuestionsValue()


class AnswerLimits(dbsettings.Group):
    """
    Defining individual settings for answers
    """
    count_answers = MinAnswersValue()


class Question(models.Model):
    """
    Basic class questions
    """
    question = models.CharField(max_length=200)
    options = QuestionLimits()

    def get_count_questions(self):
        """
        Getting count of questions for quiz
        :return: int
        """
        return Question.options.count_questions

    def __str__(self):
        return self.question


class Answer(models.Model):
    """
    Basic class answers
    """
    answer = models.CharField(max_length=60)
    question = models.ForeignKey(Question)
    correct = models.BooleanField(default=False)
    options = AnswerLimits()

    def get_count_answers(self):
        """
        Getting count of answers for all questions
        :return: int
        """
        return Answer.options.count_answers

    def __str__(self):
        return self.answer





