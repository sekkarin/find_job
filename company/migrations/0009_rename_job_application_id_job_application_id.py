# Generated by Django 4.0.4 on 2022-05-03 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_job_application_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job_application',
            old_name='Job_application_id',
            new_name='id',
        ),
    ]
