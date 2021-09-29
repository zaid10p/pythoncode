from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from . import models
# Create your views here.


def index(request):
    r = models.Question.objects.all()
    js = serializers.serialize('json',r) 

    return  HttpResponse(js, content_type="text/json-comment-filtered")


def detail(request, question_id):

    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
