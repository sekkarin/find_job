# Generated by Django 4.0.4 on 2022-04-20 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
