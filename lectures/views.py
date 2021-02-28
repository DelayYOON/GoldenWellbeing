from django.shortcuts import render
from .models import Lecture


# Create your views here.


def lecture(request):
    lectures = Lecture.objects.all().order_by('-created_at')
    context = {'lectures': lectures}
    return render(request, 'lectures/lecture.html', context)

def lecture1(request):
    lectures = Lecture.objects.all().order_by('-created_at')
    context = {'lectures': lectures}
    return render(request, 'lectures/lecture1.html', context)

def lecture2(request):
    lectures = Lecture.objects.all().order_by('-created_at')
    context = {'lectures': lectures}
    return render(request, 'lectures/lecture2.html', context)

def lecture3(request):
    lectures = Lecture.objects.all().order_by('-created_at')
    context = {'lectures': lectures}
    return render(request, 'lectures/lecture3.html', context)

def lecture4(request):
    lectures = Lecture.objects.all().order_by('-created_at')
    context = {'lectures': lectures}
    return render(request, 'lectures/lecture4.html', context)

def lecture5(request):
    lectures = Lecture.objects.all().order_by('-created_at')
    context = {'lectures': lectures}
    return render(request, 'lectures/lecture5.html', context)

def lecture6(request):
    lectures = Lecture.objects.all().order_by('-created_at')
    context = {'lectures': lectures}
    return render(request, 'lectures/lecture6.html', context)

def lecture7(request):
    lectures = Lecture.objects.all().order_by('-created_at')
    context = {'lectures': lectures}
    return render(request, 'lectures/lecture7.html', context)

def lecture8(request):
    lectures = Lecture.objects.all().order_by('-created_at')
    context = {'lectures': lectures}
    return render(request, 'lectures/lecture8.html', context)
