# Generated by Django 3.2.7 on 2021-10-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20211015_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]