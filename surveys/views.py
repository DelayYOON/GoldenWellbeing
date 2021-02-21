from django.shortcuts import render
from .models import Survey
# Create your views here.


def survey(request):
    surveys = Survey.objects.all().order_by('-created_at')
    context = {'surveys': surveys}
    return render(request, 'surveys/survey.html', context)


def presurvey(request):
    surveys = Survey.objects.all().order_by('-created_at')
    context = {'surveys': surveys}
    return render(request, 'surveys/presurvey.html', context)


def aftersurvey(request):
    surveys = Survey.objects.all().order_by('-created_at')
    context = {'surveys': surveys}
    return render(request, 'surveys/aftersurvey.html', context)
