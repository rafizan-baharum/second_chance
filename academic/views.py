from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from academic.forms import ResultbookModelForm, ResultModelForm
from academic.models import Resultbook

PER_PAGE = 10


def index_page(request):
    print('helloworld')
    qs = Resultbook.objects.all()
    context = {'resultbooks': qs}
    return render(request, "academic/index.html", context)



def resultbook_list_view(request):
    Resultbook.objects.filter()
    qs = Resultbook.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, PER_PAGE)

    try:
        resultbooks = paginator.page(page)
    except PageNotAnInteger:
        resultbooks = paginator.page(1)
    except EmptyPage:
        resultbooks = paginator.page(paginator.num_pages)

    context = {'resultbooks': resultbooks}
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
    context = {'form': form}

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('academic:resultbook_list')
    else:
        return render(request, 'academic/resultbook_create.html', context)


def result_create_modal(request, pk):
    form = ResultModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    return HttpResponse('success')
