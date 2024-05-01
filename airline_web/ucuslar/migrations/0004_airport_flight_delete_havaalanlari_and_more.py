# Generated by Django 5.0.4 on 2024-05-01 12:06

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ucuslar', '0003_havaalanlari_yolcular_yolcuucuslari'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('kalkis_tarihi', models.DateField(default=datetime.date.today)),
                ('varis_tarihi', models.DateField(default=datetime.date.today)),
                ('havayolu_adi', models.CharField(default='Default Airlines', max_length=64)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='ucuslar.airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='ucuslar.airport')),
            ],
        ),
        migrations.DeleteModel(
            name='Havaalanlari',
        ),
        migrations.RemoveField(
            model_name='yolcuucuslari',
            name='ucus',
        ),
        migrations.RemoveField(
            model_name='yolcuucuslari',
            name='yolcu',
        ),
        migrations.DeleteModel(
            name='Ucuslar',
        ),
        migrations.DeleteModel(
            name='Yolcular',
        ),
        migrations.DeleteModel(
            name='YolcuUcuslari',
        ),
    ]
