# Generated by Django 3.1.6 on 2021-05-22 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x_data', '0002_auto_20210522_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petaint',
            name='p_coved',
        ),
        migrations.AddField(
            model_name='petaint',
            name='P_CRP',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='petaint',
            name='P_HRCT',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='petaint',
            name='p_covid',
            field=models.CharField(blank=True, choices=[('Nagative', 'Nagative'), ('Positive', 'Positive')], max_length=50),
        ),
        migrations.AlterField(
            model_name='petaint',
            name='p_report',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
