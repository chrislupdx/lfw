# Generated by Django 2.0 on 2018-09-16 19:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lfw', '0004_auto_20180913_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverletter',
            name='clcopy',
            field=models.TextField(default='asdfadsf'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='company_size',
            field=models.CharField(choices=[('SL', 'SOLO'), ('TN', 'TINY'), ('LT', 'LITTLE'), ('SM', 'SMALL'), ('SM', 'SMALLISH'), ('MD', 'MEDIUM'), ('LG', 'LARGEISH'), ('CE', 'CORPORATE_ENTITY')], default=(6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25), max_length=2),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_applied',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 16, 19, 6, 9, 586630)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 16, 19, 6, 9, 586694)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_due',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 16, 19, 6, 9, 586566)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_contacted',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 16, 19, 6, 9, 586338)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_contacted',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 16, 19, 6, 9, 586444)),
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 16, 19, 6, 9, 594224)),
        ),
    ]
