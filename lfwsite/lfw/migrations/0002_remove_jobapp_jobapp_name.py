# Generated by Django 2.0 on 2018-08-30 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lfw', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapp',
            name='jobapp_name',
        ),
    ]