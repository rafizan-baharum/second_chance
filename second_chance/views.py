from django.shortcuts import render

from counseling.models import Session
from financialaid.models import Grant
from portfolio.models import Student


def home_page(request):
    studentRegistered = Student.objects.count()
    studentCounseled = Session.objects.values_list('student', flat=True).distinct().count()
    studentAided = Grant.objects.values_list('student', flat=True).distinct().count()
    qs = Student.objects.all().registered()
    context = {'students': qs,
               'studentRegistered': studentRegistered,
               'studentCounseled': studentCounseled,
               'studentAided': studentAided,
               }
    return render(request, "home.html", context)
