from django.shortcuts import render

from django.http import Http404

from .models import Questions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    questions = Questions.objects.all() 
    return render(request, 'home.html', {
        'questions': questions,
    })


def question_detail(request, question_id):
    qlist = Questions.objects.all()
    paginator = Paginator(qlist, 1)
    q = request.GET.get('q')
    qlist = paginator.get_page(q)
    try:
        question = Questions.objects.get(id=question_id)
    except Questions.DoesNotExist:
        raise Http404('question not found')
    return render(request, 'question_detail.html', {
        'question': question,
    })
