# Generated by Django 3.2 on 2022-01-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220127_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentcalander',
            name='active',
            field=models.BooleanField(blank=True, db_column='active', default=True),
            preserve_default=False,
        ),
    ]