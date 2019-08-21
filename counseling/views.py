from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from counseling.forms import SessionModelForm
from counseling.models import Session


def index_page(request):
    qs = Session.objects.all()
    context = {'sessions': qs}
    return render(request, "counseling/index.html", context)


def session_list_view(request):
    qs = Session.objects.all()
    context = {'sessions': qs}
    return render(request, 'counseling/session_list.html', context)

def session_schedule_view(request):
    qs = Session.objects.all()
    context = {'sessions': qs}
    return render(request, 'counseling/session_schedule.html', context)


def session_detail_view(request, pk):
    session = get_object_or_404(Session, pk=pk)
    student = session.student
    context = {'session': session, 'student': student}
    return render(request, 'counseling/session_detail.html', context)


def session_create_view(request):
    form = SessionModelForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/counseling/sessions/list/')
    return render(request, 'counseling/session_create.html', context)
