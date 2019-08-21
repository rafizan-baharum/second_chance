from django.contrib import admin

# Register your models here.
from portfolio.models import Student, Counselor, School, State, City

admin.site.register(State)
admin.site.register(City)
admin.site.register(Student)
admin.site.register(Counselor)
admin.site.register(School)