from django.contrib import admin
from .models import Subject, Sheet, Reference, Tutorial, Exam


admin.site.register(Subject)
admin.site.register(Sheet)
admin.site.register(Reference)
admin.site.register(Tutorial)
admin.site.register(Exam)
