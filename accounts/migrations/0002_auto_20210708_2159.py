# Generated by Django 3.2.3 on 2021-07-08 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personaldata_model',
            options={'ordering': ['PER_Customer', '-PER_Nationality'], 'verbose_name': 'Personal Data', 'verbose_name_plural': 'Personals Data'},
        ),
        migrations.RemoveField(
            model_name='personaldata_model',
            name='PER_SocialStatusMarried',
        ),
        migrations.RemoveField(
            model_name='personaldata_model',
            name='PER_SocialStatusUnmarried',
        ),
        migrations.AddField(
            model_name='personaldata_model',
            name='PER_SocialStatusEmployee',
            field=models.BooleanField(db_index=True, default=1, verbose_name='الحالة الإجتماعية -  طالب'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldata_model',
            name='PER_SocialStatusStudent',
            field=models.BooleanField(db_index=True, default=True, verbose_name='الحالة الإجتماعية - موظف'),
        ),
    ]