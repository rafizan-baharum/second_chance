from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from academic.forms import SubjectModelForm, SemesterModelForm, LevelModelForm, SchoolModelForm
from academic.models import Semester, Subject, Level
from portfolio.forms import CityModelForm, StateModelForm, CounselorModelForm
from portfolio.models import School, State, City, Counselor


def index_page(request):
    return render(request, "configuration/index.html")


def semester_list_view(request):
    qs = Semester.objects.all()
    semester_form = SemesterModelForm(None)
    context = {'semesters': qs, 'semester_form': semester_form}
    return render(request, 'configuration/semester_list.html', context)


def semester_create_modal(request):
    form = SemesterModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    else:
        return HttpResponse('Error adding semester', status=500)
    return HttpResponse('Success', status=200)


def subject_list_view(request):
    qs = Subject.objects.all()
    subject_form = SubjectModelForm(None)
    context = {'subjects': qs, 'subject_form': subject_form}
    return render(request, 'configuration/subject_list.html', context)


def subject_create_modal(request):
    form = SubjectModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    else:
        return HttpResponse('Error adding subject', status=500)
    return HttpResponse('Success', status=200)


def level_list_view(request):
    qs = Level.objects.all()
    level_form = LevelModelForm(None)
    context = {'levels': qs, 'level_form': level_form}
    return render(request, 'configuration/level_list.html', context)


def level_create_modal(request):
    form = LevelModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    else:
        return HttpResponse('Error adding subject', status=500)
    return HttpResponse('Success', status=200)


def school_list_view(request):
    qs = School.objects.all()
    school_form = SchoolModelForm(None)
    context = {'schools': qs, 'school_form': school_form}
    return render(request, 'configuration/school_list.html', context)


def school_create_modal(request):
    form = SchoolModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    else:
        return HttpResponse('Error adding school', status=500)
    return HttpResponse('Success', status=200)


def city_list_view(request):
    qs = City.objects.all()
    city_form = CityModelForm(None)
    context = {'cities': qs, 'city_form': city_form}
    return render(request, 'configuration/city_list.html', context)


def city_create_modal(request):
    form = CityModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    else:
        return HttpResponse('Error adding city', status=500)
    return HttpResponse('Success', status=200)


def state_list_view(request):
    qs = State.objects.all()
    state_form = StateModelForm(None)
    context = {'states': qs, 'state_form': state_form}
    return render(request, 'configuration/state_list.html', context)


def state_create_modal(request):
    form = StateModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    else:
        return HttpResponse('Error adding object', status=500)
    return HttpResponse('Success')


def counselor_list_view(request):
    qs = Counselor.objects.all()
    counselor_form = CounselorModelForm(None)
    context = {'counselors': qs, 'counselor_form': counselor_form}
    return render(request, 'configuration/counselor_list.html', context)


def counselor_create_modal(request):
    form = CounselorModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    else:
        return HttpResponse('Error adding object', status=500)
    return HttpResponse('Success')
