# Generated by Django 3.2.3 on 2021-07-09 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0010_auto_20210708_1600'),
        ('accounts', '0003_auto_20210708_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata_model',
            name='PER_Association',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saving.associationdata_model', verbose_name='اسم الجمعية'),
        ),
    ]
