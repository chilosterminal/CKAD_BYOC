from django.shortcuts import render

from django.http import Http404

from .models import Questions


def home(request):
    questions = Questions.objects.all() 
    return render(request, 'home.html', {
        'questions': questions,
    })


def question_detail(request, question_id):
    try:
        question = Questions.objects.get(id=question_id)
    except Questions.DoesNotExist:
        raise Http404('question not found')
    return render(request, 'question_detail.html', {
        'question': question,
    })