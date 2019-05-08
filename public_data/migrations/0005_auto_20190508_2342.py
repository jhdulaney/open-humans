# Generated by Django 2.2.1 on 2019-05-08 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("public_data", "0004_migrate_data_20190508")]

    operations = [
        migrations.RemoveField(model_name="publicdataaccess", name="data_source"),
        migrations.AlterField(
            model_name="publicdataaccess",
            name="project_membership",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="private_sharing.DataRequestProjectMember",
            ),
        ),
    ]
