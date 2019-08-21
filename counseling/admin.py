from django.contrib import admin

# Register your models here.
from counseling.models import Consultation, Session

admin.site.register(Consultation)
admin.site.register(Session)