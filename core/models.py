from django.db import models

from django.conf import settings
from datetime import datetime
from django.utils import timezone

from django.contrib.auth.models import User


YES_NO = (
        ('Yes', 'Yes'),
        ('No','No'),
    )


class LookupType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    active = models.CharField(max_length=10, choices = YES_NO)

    def __str__(self):
        return self.name


    class Meta:
        db_table = "lookuptype"
        verbose_name = 'Lookup Type'
        verbose_name_plural = 'Lookup Types'


class Lookup(models.Model):
    id = models.AutoField(primary_key=True)
    lookup_type = models.ForeignKey(LookupType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    value = models.CharField(max_length=500)
    sequence = models.IntegerField(null=True, blank=True)
    active = models.CharField(max_length=10, choices = YES_NO)

    def __str__(self):
        return self.value

    class Meta:
        db_table = "lookup"

def fileLocation(instance, filename):
        return 'uploads/{0}/{1}/{2}/{3}/{4}'.format(instance.year_level, instance.subject_code, instance.subject_type, instance.lesson_number, filename)

# def fileLocationCover(instance, filename):
#     return 'uploads/{0}/{1}/{2}/'.format(instance.year_level, instance.subject_code, instance.lesson_number)

class Subject(models.Model):
    # year_level = models.CharField(max_length=100)
    year_level = models.CharField(max_length=100, null=True, blank=True)
    subject_code = models.CharField(max_length=100)
    subject_description = models.CharField(max_length=500)
    lesson_number = models.IntegerField(null=True, blank=True)
    lesson_name = models.CharField(max_length=100)
    subject_type = models.CharField(max_length=100, null=True, blank=True)
    # title = models.CharField(max_length=100)
    # author = models.CharField(max_length=100)
    # pdf = models.FileField(upload_to='subjects/pdfs/')
    # cover = models.ImageField(upload_to='subjects/covers/', null=True, blank=True)
    cover = models.ImageField(upload_to='uploads/covers/', null=True, blank=True)
    file = models.FileField(upload_to=fileLocation, null=True, blank=True)

    # todo: must come from create/update mixin. Resolve circular reference.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='create')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='update')

    def __str__(self):
        # return self.title
        return self.subject_code

    def delete(self, *args, **kwargs):
        # self.pdf.delete()
        # self.cover.delete()
        self.file.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)


