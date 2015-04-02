from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from models import Answer, Question
import random


def get_questions(request):
    count_questions = Question().get_count_questions()
    count_answers = Answer().get_count_answers()

    question_list = Question.objects.all().order_by('?')[:int(count_questions)]

    for question in question_list:
        answers = question.answer_set.all().exclude(correct=True)[:int(count_answers) - 1]
        all_answers = question.answer_set.all()
        for answer in all_answers:
            if answer.correct:
                correct_answer = answer

        answers_list = list(answers)
        answers_list.append(correct_answer)
        random.shuffle(answers_list)
        question.answers = answers_list

    paginator = Paginator(question_list, 1)

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
    if 1 == int(number):
        del request.session['correct_answers']
        request.session['correct_answers'] = 0

    try:
        answer = get_object_or_404(Answer, pk=request.POST['answer'])
        if answer.correct:
            messages.add_message(request, messages.SUCCESS, "Correct!")
            request.session['correct_answers'] += 1
        else:
            messages.add_message(request, messages.WARNING, "Wrong!")
    except (KeyError, Answer.DoesNotExist):
        messages.add_message(request, messages.ERROR, "You didn't select a choice.")
        return HttpResponseRedirect('/quizApp/?page=' + "%s" % number)
    else:
        n = int(number) + 1
        if request.session['num_pages'] >= n:
            return HttpResponseRedirect('/quizApp/?page=' + "%s" % n)
        else:
            return render(request, 'quizApp/result.html', {
                'count_questions': request.session['num_pages'],
                'correct_answers': request.session['correct_answers']
            })



