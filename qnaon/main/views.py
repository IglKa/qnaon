from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Answer
from django.utils import timezone
from django.urls import reverse


def index(request):
    last_questions = Question.objects.all()[:10]
    return render(request, 'main/list.html', {'last_questions':last_questions})


def create_question(request):
    q = Question(question_title = request.POST['q_title'],
                 question_text = request.POST['q_text'],
                 question_author = request.POST['q_author'],
                 question_pub_date = timezone.now())
    q.save()
    return HttpResponseRedirect(reverse('main:index'))


def question_details(request, q_id):
    try:
        q = Question.objects.get(id=q_id)
    except:
        raise Http404('Ничего не найдено, сорян')
    a = q.answer_set.all()

    return render(request, 'main/question_details.html', {'question':q, 'answers':a})


def answer(request, q_id):
    try:
        q = Question.objects.get(id=q_id)
    except:
        raise Http404('Ничего не найдено, сорян')

    q.answer_set.create(answer_text = request.POST['a_text'],
                    answer_author = request.POST['a_author'],
                    answer_pub_date = timezone.now())
    return HttpResponseRedirect(reverse('main:question_details', args=(q.id,)))
