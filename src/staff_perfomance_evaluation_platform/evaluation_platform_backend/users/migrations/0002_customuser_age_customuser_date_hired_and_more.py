# Generated by Django 5.1.1 on 2024-10-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(default=0, verbose_name='age'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_hired',
            field=models.DateField(blank=True, null=True, verbose_name='date hired'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='job_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='job title'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pf_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='personnel file number'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='years_of_service',
            field=models.IntegerField(default=0, verbose_name='years of service'),
        ),
    ]
