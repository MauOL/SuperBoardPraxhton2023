# Generated by Django 4.2.6 on 2023-10-27 04:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_actividad_fecha_asignacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='fecha_asignacion',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actividad',
            name='fecha_entrega',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consultor',
            name='clave',
            field=models.CharField(default='0000', max_length=4),
            preserve_default=False,
        ),
    ]
