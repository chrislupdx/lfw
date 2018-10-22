# Generated by Django 2.0 on 2018-09-20 17:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lfw', '0008_auto_20180919_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coverlettertemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('coverlettertext', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='company_size',
            field=models.CharField(choices=[('SL', 'SOLO'), ('TN', 'TINY'), ('LT', 'LITTLE'), ('SM', 'SMALL'), ('SM', 'SMALLISH'), ('MD', 'MEDIUM'), ('LG', 'LARGEISH'), ('CE', 'CORPORATE_ENTITY')], default=(6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25), max_length=2),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_applied',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 17, 57, 18, 455513)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 17, 57, 18, 455583)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_due',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 17, 57, 18, 455450)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_contacted',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 17, 57, 18, 455244)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_contacted',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 17, 57, 18, 455331)),
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 17, 57, 18, 470220)),
        ),
        migrations.AddField(
            model_name='coverletter',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lfw.Coverlettertemplate'),
        ),
    ]