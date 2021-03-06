# Generated by Django 2.0 on 2018-09-20 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lfw', '0009_auto_20180920_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_size',
            field=models.CharField(choices=[('SL', 'SOLO'), ('TN', 'TINY'), ('LT', 'LITTLE'), ('SM', 'SMALL'), ('SM', 'SMALLISH'), ('MD', 'MEDIUM'), ('LG', 'LARGEISH'), ('CE', 'CORPORATE_ENTITY')], default=(6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25), max_length=2),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_applied',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 17, 57, 27, 159848)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 17, 57, 27, 159915)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_due',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 17, 57, 27, 159781)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_contacted',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 17, 57, 27, 159541)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_contacted',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 17, 57, 27, 159630)),
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 17, 57, 27, 172830)),
        ),
    ]
