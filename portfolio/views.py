from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum, Q
from django.db.models.functions import TruncYear
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from financialaid.models import Grant
from portfolio.forms import StudentModelForm
from portfolio.models import Student

PER_PAGE = 10


def index_page(request):
    qs = Student.objects.all().registered()
    context = {'students': qs}
    return render(request, "portfolio/index.html", context)


def student_list_view(request):
    qs = Student.objects.all().registered()
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, 10)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    context = {'students': students}
    return render(request, 'portfolio/student_list.html', context)


def student_search_view(request):
    keyword = request.GET.get('keyword', '')
    qs = Student.objects.filter((Q(name__icontains=keyword) |
                                 Q(nick_name__icontains=keyword) |
                                 Q(nric_no__icontains=keyword) |
                                 Q(address1__icontains=keyword) |
                                 Q(address2__icontains=keyword) |
                                 Q(address3__icontains=keyword)
                                 ))
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, 10)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    context = {'students': students, 'keyword': keyword}
    return render(request, 'portfolio/student_search.html', context)


def student_detail_view(request, nric_no):
    student = get_object_or_404(Student, nric_no=nric_no)
    context = {'student': student}
    return render(request, 'portfolio/student_detail.html', context)


def student_summary_view(request, nric_no):
    student = get_object_or_404(Student, nric_no=nric_no)
    context = {'student': student}
    return render(request, 'portfolio/student_summary.html', context)


def student_academic_view(request, nric_no):
    student = get_object_or_404(Student, nric_no=nric_no)
    resultbooks = student.resultbooks.all
    context = {'student': student, 'resultbooks': resultbooks}
    return render(request, 'portfolio/student_academic.html', context)


def student_counseling_view(request, nric_no):
    student = get_object_or_404(Student, nric_no=nric_no)
    sessions = student.sessions.all
    context = {'student': student, 'sessions': sessions}
    return render(request, 'portfolio/student_counseling.html', context)


def student_financialaid_view(request, nric_no):
    student = get_object_or_404(Student, nric_no=nric_no)
    summaryGrants = Grant.objects.filter(student=student).annotate(month=TruncYear('disbursed_date')).values(
        'disbursed_date').annotate(sum=Sum('amount')).order_by()
    print(summaryGrants)
    grants = student.grants.all
    context = {'student': student, 'summaryGrants': summaryGrants, 'grants': grants}
    return render(request, 'portfolio/student_financialaid.html', context)


def student_create_view(request):
    form = StudentModelForm(request.POST or None, request.FILES or None)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/portfolio/students/list/')
    return render(request, 'portfolio/student_create.html', context)


def student_update_view(request, nric_no):
    student = get_object_or_404(Student, nric_no=nric_no)
    form = StudentModelForm(request.POST or None, request.FILES or None, instance=student)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/portfolio/students/list/')
    return render(request, 'portfolio/student_update.html', context)
