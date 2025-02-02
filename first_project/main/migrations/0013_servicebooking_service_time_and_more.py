# Generated by Django 5.0.6 on 2024-06-19 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_servicebooking_delete_bookservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicebooking',
            name='service_time',
            field=models.TimeField(default='00:00', verbose_name='Время оказания услуги'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicebooking',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.person', verbose_name='Гость'),
        ),
        migrations.AlterField(
            model_name='servicebooking',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.services', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='servicebooking',
            name='service_date',
            field=models.DateField(verbose_name='Дата оказания услуги'),
        ),
    ]
