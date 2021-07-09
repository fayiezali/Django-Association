# Generated by Django 3.2.3 on 2021-07-08 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0009_auto_20210707_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housingdata_model',
            name='HOU_Association',
        ),
        migrations.RemoveField(
            model_name='housingdata_model',
            name='HOU_Customer',
        ),
        migrations.RemoveField(
            model_name='personaldata_model',
            name='PER_Association',
        ),
        migrations.RemoveField(
            model_name='personaldata_model',
            name='PER_Customer',
        ),
        migrations.DeleteModel(
            name='FinancialData_MODEL',
        ),
        migrations.DeleteModel(
            name='HousingData_MODEL',
        ),
        migrations.DeleteModel(
            name='PersonalData_MODEL',
        ),
    ]