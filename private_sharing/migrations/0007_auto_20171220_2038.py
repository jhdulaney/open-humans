# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-12-20 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('open_humans', '0006_userevent_event_type'),
        ('private_sharing', '0006_auto_20161102_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=15, verbose_name=(('created-account', 'created-account'), ('joined-project', 'joined-project'), ('publicly-shared', 'publicly-shared')))),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='open_humans.Member')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='private_sharing.DataRequestProject')),
            ],
        ),
        migrations.AlterField(
            model_name='oauth2datarequestproject',
            name='redirect_url',
            field=models.CharField(help_text='The return URL for our "authorization code" OAuth2 grant\n        process. You can <a target="_blank" href="/direct-sharing/oauth2-setup/#setup-oauth2-authorization">read more about OAuth2\n        "authorization code" transactions here</a>.', max_length=256, verbose_name='Redirect URL'),
        ),
    ]
