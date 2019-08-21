from django.contrib import admin

# Register your models here.
from academic.models import Semester, Subject, Resultbook, Result, Level

admin.site.register(Semester)
admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(Resultbook)
admin.site.register(Result)
