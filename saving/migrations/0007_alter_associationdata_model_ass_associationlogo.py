# Generated by Django 3.2.3 on 2021-06-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0006_alter_associationdata_model_ass_associationlogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationdata_model',
            name='ASS_AssociationLogo',
            field=models.ImageField(db_index=True, default='Default_Image.png', upload_to='AssociationData_Image/', verbose_name='شعار الجمعية'),
        ),
    ]
