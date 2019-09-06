from django.db.models import Sum
from django.db.models.functions import TruncYear
from django.shortcuts import render

from academic.models import Resultbook
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


def report_page(request, nric_no):
    student = Student.objects.filter(nric_no=nric_no).first()
    totalGrant = Grant.objects.filter(student=student).aggregate(sum=Sum('amount'))
    recentResultbook = Resultbook.objects.filter(student=student).order_by('-created_date').first()

    summaryGrants = Grant.objects.filter(student=student).annotate(month=TruncYear('disbursed_date')).values(
        'disbursed_date').annotate(sum=Sum('amount')).order_by()
    recentResultbooks = Resultbook.objects.filter(student=student).order_by('-created_date')[:5]

    context = {
        'student': student,
        'totalGrant': totalGrant,
        'summaryGrants': summaryGrants,
        'recentResultbook': recentResultbook,
        'recentResultbooks': recentResultbooks
    }
    return render(request, "report.html", context)
