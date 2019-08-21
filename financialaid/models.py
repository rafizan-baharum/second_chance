from django.conf import settings
from django.db import models
from django.db.models import Q

# Create your models here.
from portfolio.models import Student

"""Choices"""

PURPOSE_CHOICES = (
    ('TUITION', 'TUITION'),
    ('STIPEND', 'STIPEND'),
    ('OTHERS', 'OTHERS'),
)

"""Grant"""


class GrantQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
            Q(student__name__icontains=query),
        )

        return self.filter(lookup)


class GrantManager(models.Manager):
    def get_queryset(self):
        return GrantQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Grant(models.Model):  # Grant_set -> queryset
    # id = models.IntegerField() # pk
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL, related_name='grants')
    donor = models.CharField(max_length=120)
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    remarks = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    approved_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    disbursed_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = GrantManager()

    class Meta:
        ordering = ['approved_date']

    def get_absolute_url(self):
        return f"/financialaid/grants/{self.id}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return 'Grant: ' + self.student.name + ':' + self.amount.__str__()
