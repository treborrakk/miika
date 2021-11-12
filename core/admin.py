from django.contrib import admin
from .models import Subject, LookupType, Lookup
# from .models import Subject

class LookupAdmin(admin.ModelAdmin):
    list_display = ('id', 'lookup_type', 'name', 'description', 'value', 'sequence', 'active')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('year_level', 'subject_code', 'subject_description', 'lesson_number', 'lesson_name', 'cover', 'file')


admin.site.register(Subject,SubjectAdmin)
admin.site.register(LookupType)
admin.site.register(Lookup,LookupAdmin)
