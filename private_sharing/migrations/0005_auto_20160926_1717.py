# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-26 17:17

from django.db import migrations


def migrate_completed(apps, *args):
    ProjectDataFile = apps.get_model('private_sharing', 'ProjectDataFile')

    ProjectDataFile.objects.all().update(completed=True)


class Migration(migrations.Migration):

    dependencies = [
        ('private_sharing', '0004_projectdatafile_completed'),
    ]

    operations = [
        migrations.RunPython(migrate_completed),
    ]
