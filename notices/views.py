from django.shortcuts import render
from .models import Notice


# Create your views here.


def index(request):
    notices = Notice.objects.all().order_by('-created_at')
    context = {'notices': notices}
    return render(request, 'notices/index.html', context)
