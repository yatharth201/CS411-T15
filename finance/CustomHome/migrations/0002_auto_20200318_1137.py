# Generated by Django 3.0.4 on 2020-03-18 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CustomHome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regulartransaction',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nonregulartransaction',
            name='time',
            field=models.DateField(),
        ),
    ]
