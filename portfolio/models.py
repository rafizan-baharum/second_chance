from django.conf import settings
from django.db import models
from django.db.models import Q

# Create your models here.

User = settings.AUTH_USER_MODEL

"""Choices"""

GENDER_CHOICES = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'))

RACE_CHOICES = (
    ('MALAY', 'MALAY'),
    ('CHINESE', 'CHINESE'),
    ('INDIAN', 'INDIAN'),
    ('OTHERS', 'OTHERS'),)

RELIGION_CHOICES = (
    ('ISLAM', 'ISLAM'),
    ('BUDDHA', 'BUDDHA'),
    ('CHRISTIAN', 'CHRISTIAN'),
    ('HINDU', 'HINDU'),
    ('OTHERS', 'OTHERS'),)

BANK_CHOICES = (
    ('MAYBANK', 'MAYBANK'),
    ('BANK ISLAM', 'BANK ISLAM'),
    ('AFFIN BANK', 'AFFIN BANK'),
    ('OTHERS', 'OTHERS'),)

"""State"""


class StateQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
                Q(nric_no__icontains=query) |
                Q(name__icontains=query)
        )
        return self.filter(lookup)


class StateManager(models.Manager):
    def get_queryset(self):
        return StateQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class State(models.Model):
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False, unique=True)
    name = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = StateManager()

    class Meta:
        ordering = ['-modified_date']
        verbose_name_plural = "States"

    def get_absolute_url(self):
        return f"/portfolio/states/{self.code}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return f"{self.code}:{self.name}"


"""City"""


class CityQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
            Q(nric_no__icontains=query)|
            Q(name__icontains=query)
        )
        return self.filter(lookup)


class CityManager(models.Manager):
    def get_queryset(self):
        return CityQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class City(models.Model):
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False, unique=True)
    name = models.CharField(max_length=120)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = CityManager()

    class Meta:
        ordering = ['-modified_date']
        verbose_name_plural = "Cities"

    def get_absolute_url(self):
        return f"/portfolio/citys/{self.code}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return f"{self.code}:{self.name}"


"""School"""


class SchoolQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
            Q(nric_no__icontains=query)|
            Q(name__icontains=query)
        )
        return self.filter(lookup)


class SchoolManager(models.Manager):
    def get_queryset(self):
        return SchoolQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class School(models.Model):
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False, unique=True)
    name = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = SchoolManager()

    class Meta:
        ordering = ['-modified_date']
        verbose_name_plural = "Schools"

    def get_absolute_url(self):
        return f"/portfolio/schools/{self.code}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return f"{self.code}:{self.name}"


"""Student"""


class StudentQuerySet(models.QuerySet):
    def registered(self):
        return self

    def search(self, query):
        lookup = (
            Q(nric_no__icontains=query),
            Q(name__icontains=query)
        )

        return self.filter(lookup)


class StudentManager(models.Manager):
    def get_queryset(self):
        return StudentQuerySet(self.model, using=self._db)

    def registered(self):
        return self.get_queryset().registered()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().registered().search(query)


class Student(models.Model):
    # id = models.IntegerField() # pk
    # creator    = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/no-img.jpg')
    nric_no = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=120)
    nick_name = models.CharField(max_length=60, blank=False)
    address1 = models.CharField(max_length=120, blank=False)
    address2 = models.CharField(max_length=120, blank=False)
    address3 = models.CharField(max_length=120, blank=True)
    birth_date = models.DateField(null=False, blank=False)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    race = models.CharField(max_length=60, choices=RACE_CHOICES)
    religion = models.CharField(max_length=60, choices=RELIGION_CHOICES)
    school = models.ForeignKey(School, null=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)

    bank = models.CharField(max_length=60, choices=BANK_CHOICES)
    bank_account_no = models.CharField(max_length=60)

    father_nric_no = models.CharField(max_length=120)
    father_name = models.CharField(max_length=120)
    father_race = models.CharField(max_length=60, choices=RACE_CHOICES)
    father_religion = models.CharField(max_length=60, choices=RELIGION_CHOICES)
    father_income = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    mother_nric_no = models.CharField(max_length=120)
    mother_name = models.CharField(max_length=120)
    mother_race = models.CharField(max_length=60, choices=RACE_CHOICES)
    mother_religion = models.CharField(max_length=60, choices=RELIGION_CHOICES)
    mother_income = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = StudentManager()

    class Meta:
        ordering = ['-modified_date']
        verbose_name_plural = "Students"

    def get_absolute_url(self):
        return f"/portfolio/students/{self.nric_no}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return f"{self.name} ({self.nric_no})"


"""Counselor"""


class CounselorQuerySet(models.QuerySet):

    def search(self, query):
        lookup = (
            Q(nric_no__icontains=query),
            Q(name__icontains=query)
        )

        return self.filter(lookup)


class CounselorManager(models.Manager):
    def get_queryset(self):
        return CounselorQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Counselor(models.Model):  # Counselor_set -> queryset
    # id = models.IntegerField() # pk
    nric_no = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=120)
    address1 = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120)
    address3 = models.CharField(max_length=120)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = CounselorManager()

    class Meta:
        ordering = ['-modified_date']
        verbose_name_plural = "Counselors"

    def get_absolute_url(self):
        return f"/portfolio/counselors/{self.nric_no}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return f"{self.name} ({self.nric_no})"
