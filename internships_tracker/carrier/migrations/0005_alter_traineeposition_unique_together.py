# Generated by Django 3.2.9 on 2022-04-03 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0004_auto_20220328_0136'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='traineeposition',
            unique_together={('job_code', 'no_id')},
        ),
    ]
