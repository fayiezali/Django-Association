# Generated by Django 3.2.3 on 2021-06-19 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0004_alter_associationdata_model_ass_associationlogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationdata_model',
            name='ASS_AssociationLogo',
            field=models.ImageField(blank=True, db_index=True, null=True, upload_to='AssociationData_Image/', verbose_name='شعار الجمعية'),
        ),
    ]
