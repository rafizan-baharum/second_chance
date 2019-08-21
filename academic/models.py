from django.conf import settings
from django.db import models
from django.db.models import Q

# Create your models here.
from portfolio.models import Student, School

"""Choices"""

GRADE_CHOICES = (
    ('A+', 'A+'),
    ('A', 'A'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B', 'B'),
    ('B-', 'B-'),
    ('C+', 'C+'),
    ('C', 'C'),
    ('C-', 'C-'),
    ('D+', 'D+'),
    ('D', 'D'),
    ('D-', 'D-'),
    ('E+', 'E+'),
    ('E', 'E'),
    ('E-', 'E-'),
    ('F', 'F'))

"""Semester"""


class SemesterQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
            Q(code__icontains=query),
            Q(name__icontains=query)
        )
        return self.filter(lookup)


class SemesterManager(models.Manager):
    def get_queryset(self):
        return SemesterQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Semester(models.Model):
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = SemesterManager()

    class Meta:
        ordering = ['-modified_date']

    def get_absolute_url(self):
        return f"/academic/semesters/{self.code}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return f"{self.code}:{self.name}"


"""Level"""


class LevelQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
            Q(code__icontains=query),
            Q(name__icontains=query)
        )
        return self.filter(lookup)


class LevelManager(models.Manager):
    def get_queryset(self):
        return LevelQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Level(models.Model):
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = LevelManager()

    class Meta:
        ordering = ['-modified_date']

    def get_absolute_url(self):
        return f"/academic/levels/{self.code}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return f"{self.code}:{self.name}"


"""Subject"""


class SubjectQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
            Q(nric_no__icontains=query),
            Q(name__icontains=query)
        )
        return self.filter(lookup)


class SubjectManager(models.Manager):
    def get_queryset(self):
        return SubjectQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Subject(models.Model):
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = SubjectManager()

    class Meta:
        ordering = ['-modified_date']

    def get_absolute_url(self):
        return f"/academic/subjects/{self.code}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return f"{self.code}:{self.name}"


"""
Resultbook
"""


class ResultbookQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
            Q(student__name__icontains=query),
            Q(school__name__icontains=query),
        )
        return self.filter(lookup)


class ResultbookManager(models.Manager):
    def get_queryset(self):
        return ResultbookQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Resultbook(models.Model):
    # id = models.IntegerField() # pk
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL, related_name='resultbooks')
    semester = models.ForeignKey(Semester, null=True, on_delete=models.SET_NULL)
    level = models.ForeignKey(Level, null=True, on_delete=models.SET_NULL)
    school = models.ForeignKey(School, null=True, on_delete=models.SET_NULL)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = ResultbookManager()

    class Meta:
        ordering = ['-modified_date']

    def get_absolute_url(self):
        return f"/academic/resultbooks/{self.id}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return f"{self.semester.code}:{self.student.nric_no}:{self.school.code}"


"""
Result
"""


class ResultQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
            Q(subject__name__icontains=query)
        )
        return self.filter(lookup)


class ResultManager(models.Manager):
    def get_queryset(self):
        return ResultQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Result(models.Model):
    # id = models.IntegerField() # pk
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey(Resultbook, null=True, on_delete=models.SET_NULL, related_name='results')
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = ResultManager()

    class Meta:
        ordering = ['-modified_date']

    def get_absolute_url(self):
        return f"/academic/results/{self.id}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return 'Result: ' + self.subject.code + ':' + self.grade
