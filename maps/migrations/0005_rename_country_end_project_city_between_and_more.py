# Generated by Django 4.0.5 on 2023-08-09 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_project_country_end_project_country_start_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='country_end',
            new_name='city_between',
        ),
        migrations.RemoveField(
            model_name='project',
            name='country_start',
        ),
        migrations.RemoveField(
            model_name='project',
            name='distance',
        ),
        migrations.RemoveField(
            model_name='project',
            name='docsize4',
        ),
        migrations.RemoveField(
            model_name='project',
            name='docsize5',
        ),
        migrations.RemoveField(
            model_name='project',
            name='price',
        ),
        migrations.RemoveField(
            model_name='project',
            name='rows',
        ),
        migrations.RemoveField(
            model_name='project',
            name='state_end',
        ),
        migrations.RemoveField(
            model_name='project',
            name='state_start',
        ),
    ]
