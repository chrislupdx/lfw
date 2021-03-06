# Generated by Django 2.0 on 2018-09-07 21:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True, null=True)),
                ('IPO', models.BooleanField()),
                ('company_size', models.CharField(choices=[('SL', 'SOLO'), ('TN', 'TINY'), ('LT', 'LITTLE'), ('SM', 'SMALL'), ('SM', 'SMALLISH'), ('MD', 'MEDIUM'), ('LG', 'LARGEISH'), ('CE', 'CORPORATE_ENTITY')], default=(6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25), max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=25, null=True)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(blank=True, max_length=70, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('years_at_company', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=50)),
                ('date_met', models.DateTimeField(blank=True, null=True)),
                ('last_soft_communication', models.DateTimeField(blank=True, null=True)),
                ('first_contacted', models.DateTimeField(default=datetime.datetime(2018, 9, 7, 21, 56, 42, 234426))),
                ('last_contacted', models.DateTimeField(default=datetime.datetime(2018, 9, 7, 21, 56, 42, 234513))),
                ('date_rolecreated', models.DateTimeField(blank=True, null=True)),
                ('date_due', models.DateTimeField(default=datetime.datetime(2018, 9, 7, 21, 56, 42, 234636))),
                ('date_applied', models.DateTimeField(default=datetime.datetime(2018, 9, 7, 21, 56, 42, 234699))),
                ('date_created', models.DateTimeField(default=datetime.datetime(2018, 9, 7, 21, 56, 42, 234769))),
                ('app_contact_status', models.CharField(choices=[('UD', 'UNDEFINED'), ('SC', 'Social'), ('AC', 'Ancillary'), ('RF', 'Job_Referral'), ('MG', 'Hiring Manager')], default=5, max_length=2)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lfw.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coverletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jobapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('company', models.CharField(default='No company', max_length=50)),
                ('followup_touches', models.IntegerField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('first_contacted', models.DateTimeField(blank=True, null=True)),
                ('last_contacted', models.DateTimeField(blank=True, null=True)),
                ('date_rolecreated', models.DateTimeField(blank=True, null=True)),
                ('date_due', models.DateTimeField(blank=True, null=True)),
                ('date_applied', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2018, 9, 7, 21, 56, 42, 241947))),
                ('pipeline_status', models.CharField(choices=[('PS', 'PROSPECT'), ('RO', 'REACHEDOUT'), ('QD', 'QUALIFIED'), ('SN', 'SCREENING')], default='PS', max_length=2)),
                ('contact', models.ManyToManyField(blank=True, to='lfw.Contact')),
                ('coverletter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lfw.Coverletter')),
                ('referred_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referred_by', to='lfw.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='jobapp',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lfw.Resume'),
        ),
        migrations.AddField(
            model_name='jobapp',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
