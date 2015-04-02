from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from models import Answer, Question
import random


def get_questions(request):
    """
    Method for loading all questions
    """
    count_questions = Question().get_count_questions()  # getting count of questions
    count_answers = Answer().get_count_answers()  # getting count of answers for question

    question_list = Question.objects.all().order_by('?')[:int(count_questions)]  # random questions

    for question in question_list:
        answers = question.answer_set.all().exclude(correct=True)[:int(count_answers) - 1]
        all_answers = question.answer_set.all()
        for answer in all_answers:
            if answer.correct:
                correct_answer = answer  # getting correct answer

        answers_list = list(answers)
        answers_list.append(correct_answer)
        random.shuffle(answers_list)  # random answers
        question.answers = answers_list

    paginator = Paginator(question_list, 1)  # one question for page

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    request.session['num_pages'] = paginator.num_pages

    return render(request, 'quizApp/index.html', {
        'questions': questions,
    })


def vote(request, number):
    """
    Checking answer for given question
    :param number: int
    """
    if 1 == int(number):
        del request.session['correct_answers']
        request.session['correct_answers'] = 0

    try:
        answer = get_object_or_404(Answer, pk=request.POST['answer'])  # getting user answer
        if answer.correct:  # check if answer is correct
            messages.add_message(request, messages.SUCCESS, "Correct!")
            request.session['correct_answers'] += 1  # getting correct answers
        else:
            messages.add_message(request, messages.WARNING, "Wrong!")
    except (KeyError, Answer.DoesNotExist):  # check if user input value is correct
        messages.add_message(request, messages.ERROR, "You didn't select a choice.")
        return HttpResponseRedirect('/quizApp/?page=' + "%s" % number)
    else:
        n = int(number) + 1
        if request.session['num_pages'] >= n:  # check if question is last
            return HttpResponseRedirect('/quizApp/?page=' + "%s" % n)
        else:
            return render(request, 'quizApp/result.html', {
                'count_questions': request.session['num_pages'],
                'correct_answers': request.session['correct_answers']
            })



