# Generated by Django 3.2 on 2022-09-24 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_personalcharacteristics_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalcharacteristics',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
