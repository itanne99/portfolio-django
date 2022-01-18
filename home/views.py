from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Projects


def index(request):
    projects = Projects.objects.order_by('-name')
    template = loader.get_template('index.html')
    context = {
        'title': "Home",
        'projects': projects,
    }
    return HttpResponse(template.render(context, request))
