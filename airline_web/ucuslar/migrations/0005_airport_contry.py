# Generated by Django 5.0.4 on 2024-05-01 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ucuslar', '0004_airport_flight_delete_havaalanlari_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='contry',
            field=models.CharField(default='country', max_length=32),
        ),
    ]
