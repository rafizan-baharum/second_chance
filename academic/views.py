from django.shortcuts import render, get_object_or_404

# Create your views here.
from academic.forms import ResultbookModelForm, ResultModelForm
from academic.models import Resultbook


def index_page(request):
    qs = Resultbook.objects.all()
    context = {'resultbooks': qs}
    return render(request, "academic/index.html", context)


def resultbook_list_view(request):
    qs = Resultbook.objects.all()
    context = {'resultbooks': qs}
    return render(request, 'academic/resultbook_list.html', context)


def resultbook_summary_view(request, pk):
    resultbook = get_object_or_404(Resultbook, pk=pk)
    student = resultbook.student
    context = {'resultbook': resultbook, 'student': student}
    return render(request, 'academic/resultbook_summary.html', context)


def resultbook_detail_view(request, pk):
    resultbook = get_object_or_404(Resultbook, pk=pk)
    student = resultbook.student
    resultbooks = student.resultbooks.all
    result_form = ResultModelForm(None)
    context = {'resultbook': resultbook, 'student': student, 'resultbooks': resultbooks, 'result_form': result_form}
    return render(request, 'academic/resultbook_detail.html', context)


def resultbook_create_view(request):
    form = ResultbookModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ResultbookModelForm()
    context = {'form': form}
    return render(request, 'academic/resultbook_create.html', context)


def result_create_view(request):
    form = ResultModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    return reversed(request, 'academic/resultbook_detail.html')
