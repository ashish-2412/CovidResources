# Generated by Django 3.1.4 on 2021-04-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20210423_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidresource',
            name='date_added',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
