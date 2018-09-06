# Generated by Django 2.0 on 2018-09-06 01:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lfw', '0002_auto_20180904_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverletter',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 1, 51, 20, 358997)),
        ),
        migrations.AddField(
            model_name='resume',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 1, 51, 20, 356739)),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_size',
            field=models.CharField(choices=[('SL', 'SOLO'), ('TN', 'TINY'), ('LT', 'LITTLE'), ('SM', 'SMALL'), ('SM', 'SMALLISH'), ('MD', 'MEDIUM'), ('LG', 'LARGEISH'), ('CE', 'CORPORATE_ENTITY')], default=(6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25), max_length=2),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_applied',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 1, 51, 20, 352548)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 1, 51, 20, 352628)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_due',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 1, 51, 20, 352485)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_contacted',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 1, 51, 20, 352264)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_contacted',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 1, 51, 20, 352361)),
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='date_applied',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 1, 51, 20, 361763)),
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 1, 51, 20, 361826)),
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='date_due',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 1, 51, 20, 361686)),
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='first_contacted',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 1, 51, 20, 361452)),
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='last_contacted',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 1, 51, 20, 361546)),
        ),
    ]
