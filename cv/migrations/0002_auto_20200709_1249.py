# Generated by Django 2.1.15 on 2020-07-09 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cv',
            new_name='Cv_section',
        ),
        migrations.AlterModelOptions(
            name='cv_section',
            options={'verbose_name_plural': 'cv_sections'},
        ),
    ]
