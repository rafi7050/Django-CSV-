from django.contrib import admin

# Register your models here.

from core.models import Teacher, Csv

admin.site.register(Teacher)
admin.site.register(Csv)
