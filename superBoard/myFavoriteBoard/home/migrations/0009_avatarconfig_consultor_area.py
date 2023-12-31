# Generated by Django 4.2.6 on 2023-10-29 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_totalvalor_calculototales_total_valor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvatarConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_consultor', models.IntegerField()),
                ('cualidades', models.CharField(max_length=180)),
                ('nombre_foto', models.CharField(max_length=100)),
                ('color_fondo', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='consultor',
            name='area',
            field=models.CharField(default=1, max_length=35),
            preserve_default=False,
        ),
    ]
