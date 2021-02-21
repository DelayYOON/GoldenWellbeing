from django.shortcuts import render
from .models import Lecture


# Create your views here.


def lecture(request):
    lectures = Lecture.objects.all().order_by('-created_at')
    context = {'lectures': lectures}
    return render(request, 'lectures/lecture.html', context)
# Create your views here.
