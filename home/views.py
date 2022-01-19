from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Projects, FrontEndSkills, BackEndSkills, DesignSkills


def index(request):
    projects = Projects.objects.order_by('-name')
    frontEndSkills = FrontEndSkills.objects.order_by('-skill')
    backEndSkills = BackEndSkills.objects.order_by('-skill')
    designSkills = DesignSkills.objects.order_by('-skill')
    template = loader.get_template('index.html')
    context = {
        'title': "Home",
        'projects': projects,
        'frontEndSkills': frontEndSkills,
        'backEndSkills': backEndSkills,
        'designSkills': designSkills,
    }
    return HttpResponse(template.render(context, request))
