from django.conf import settings
from django.db import models
from django.db.models import Q

from portfolio.models import Student, Counselor

# Create your models here.

User = settings.AUTH_USER_MODEL


# Consultation


class ConsultationQuerySet(models.QuerySet):

    def search(self, query):
        lookup = (
            Q(student__name__icontains=query),
            Q(counselor__name__icontains=query)
        )

        return self.filter(lookup)


class ConsultationManager(models.Manager):
    def get_queryset(self):
        return ConsultationQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Consultation(models.Model):  # Session_set -> queryset
    # id = models.IntegerField() # pk
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    counselor = models.ForeignKey(Counselor, null=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = ConsultationManager()

    class Meta:
        ordering = ['-modified_date']

    def get_absolute_url(self):
        return f"/counseling/consultations/{self.id}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"


"""Session"""


class SessionQuerySet(models.QuerySet):

    def search(self, query):
        lookup = (
            Q(student__name__icontains=query),
            Q(counselor__name__icontains=query)
        )

        return self.filter(lookup)


class SessionManager(models.Manager):
    def get_queryset(self):
        return SessionQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Session(models.Model):  # Session_set -> queryset
    # id = models.IntegerField() # pk
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL, related_name='sessions')
    counselor = models.ForeignKey(Counselor, null=True, on_delete=models.SET_NULL)
    remarks = models.TextField()
    venue = models.CharField(max_length=120)
    counseled_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = SessionManager()

    class Meta:
        ordering = ['-counseled_date', '-modified_date']

    def get_absolute_url(self):
        return f"/counseling/sessions/{self.id}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/update"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
