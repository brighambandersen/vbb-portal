# Generated by Django 3.0.8 on 2020-08-12 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200811_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='mentee',
        ),
        migrations.DeleteModel(
            name='MenteeProfile',
        ),
    ]