from django.contrib import admin
from .models import Subject, LookupType, Lookup
# from .models import Subject

class LookupAdmin(admin.ModelAdmin):
    fields = ('lookup_type', 'name', 'description', 'value', 'sequence', 'active')
    list_display = ('id', 'lookup_type', 'name', 'description', 'value', 'sequence', 'active')

class LookupTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',  'active')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('year_level', 'subject_code', 'subject_description', 'lesson_number', 'lesson_name', 'subject_type',
                    'cover', 'file')


admin.site.register(Subject,SubjectAdmin)
admin.site.register(LookupType,LookupTypeAdmin)
admin.site.register(Lookup,LookupAdmin)
