from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Answer
from django.utils import timezone


def index(request):
    last_questions = Question.objects.all()[:10]
    return render(request, 'main/list.html', {'last_questions':last_questions})


def create_question(request):
    q = Question(question_title = request.POST['q_title'],
                 question_text = request.POST['q_text'],
                 question_author = request.POST['q_author'],
                 question_pub_date = timezone.now())
    q.save()
    return HttpResponseRedirect(revers('index'))


def question_details(request, q_id):
    try:
        q = Question.objects.get(id=q_id)
    except:
        return Http404('Ничего не нацдено, сорян')

    return render(request, 'main/question_details.html', {'question':q})
