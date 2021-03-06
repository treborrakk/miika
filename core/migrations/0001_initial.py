# Generated by Django 3.2.7 on 2021-11-15 06:51

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LookupType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('active', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
            ],
            options={
                'verbose_name': 'Lookup Type',
                'verbose_name_plural': 'Lookup Types',
                'db_table': 'lookuptype',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_level', models.CharField(blank=True, max_length=100, null=True)),
                ('subject_code', models.CharField(max_length=100)),
                ('subject_description', models.CharField(max_length=500)),
                ('lesson_number', models.IntegerField(blank=True, null=True)),
                ('lesson_name', models.CharField(max_length=100)),
                ('subject_type', models.CharField(blank=True, max_length=100, null=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='uploads/covers/')),
                ('file', models.FileField(blank=True, null=True, upload_to=core.models.fileLocation)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='create', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='update', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lookup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('value', models.CharField(max_length=500)),
                ('sequence', models.IntegerField(blank=True, null=True)),
                ('active', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('lookup_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.lookuptype')),
            ],
            options={
                'db_table': 'lookup',
            },
        ),
    ]
