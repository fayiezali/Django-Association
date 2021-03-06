# Generated by Django 3.2.3 on 2021-07-07 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saving', '0008_alter_associationdata_model_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='associationdata_model',
            options={'ordering': ['ASS_NameAssociation', '-ASS_Mobile'], 'verbose_name': 'Association Data', 'verbose_name_plural': 'Associations Data'},
        ),
        migrations.AlterField(
            model_name='financialdata_model',
            name='FIN_Customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المشترك'),
        ),
        migrations.AlterField(
            model_name='housingdata_model',
            name='HOU_Customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المشترك'),
        ),
        migrations.AlterField(
            model_name='personaldata_model',
            name='PER_Customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المشترك'),
        ),
    ]
