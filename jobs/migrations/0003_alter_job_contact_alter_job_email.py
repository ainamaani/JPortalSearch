# Generated by Django 4.2.7 on 2023-11-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_job_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='contact',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='job',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
