from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from financialaid.forms import GrantModelForm
from financialaid.models import Grant


def index_page(request):
    qs = Grant.objects.order_by('-created_date')[:10]
    context = {'grants': qs}
    return render(request, "financialaid/index.html", context)


def grant_list_view(request):
    qs = Grant.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, 10)
    try:
        grants = paginator.page(page)
    except PageNotAnInteger:
        grants = paginator.page(1)
    except EmptyPage:
        grants = paginator.page(paginator.num_pages)
    context = {'grants': grants}
    return render(request, 'financialaid/grant_list.html', context)


def grant_summary_view(request, pk):
    grant = get_object_or_404(Grant, pk=pk)
    student = grant.student
    context = {'grant': grant, 'student': student}
    return render(request, 'financialaid/grant_summary.html', context)


def grant_detail_view(request, pk):
    grant = get_object_or_404(Grant, pk=pk)
    student = grant.student
    grants = student.grants.all
    context = {'grant': grant, 'student': student, 'grants': grants}
    return render(request, 'financialaid/grant_detail.html', context)


def grant_request_view(request, pk):
    grant = get_object_or_404(Grant, pk=pk)
    student = grant.student
    context = {'grant': grant, 'student': student}
    return render(request, 'financialaid/grant_detail.html', context)


def grant_create_view(request):
    form = GrantModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = GrantModelForm()
        return redirect('/financialaid/grants/list/')
    context = {'form': form}
    return render(request, 'financialaid/grant_create.html', context)


def grant_update_view(request, pk):
    grant = get_object_or_404(Grant, pk=pk)
    form = GrantModelForm(request.POST or None, instance=grant)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = GrantModelForm()
        return redirect('/financialaid/grants/list/')
    context = {'form': form}
    return render(request, 'financialaid/grant_update.html', context)
