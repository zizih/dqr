from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Page

# Create your views here.


def default(request):
    return HttpResponse("Well come ..");


def quest(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'quest.html', context)


def index(request):
    page_list = Page.objects.all()
    context = {'page_list': page_list}
    return render(request, 'index.html', context)


def encode(request):
    encode_text = request.GET.get('encode_text', 'sb')
    context = {'encode_text': encode_text}
    return render(request, 'encode.html', context)
