# Generated by Django 3.2.7 on 2021-10-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211011_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
