from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

from core.models import Film


def index(request):
    films = Film.objects.all()
    context = {'films': films, 'title': 'Список фильмов'}
    return render(request, template_name='core/index.html', context=context)