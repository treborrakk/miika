# Generated by Django 3.2.7 on 2021-10-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_subject_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='lesson_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]