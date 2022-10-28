# Generated by Django 3.2 on 2022-10-27 22:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_alter_devices_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='type',
            field=models.CharField(choices=[('device_semg', 'SEMG'), ('device_inertial', 'INERTIAL'), ('device_ir', 'IR')], default=None, max_length=256),
        ),
        migrations.AlterUniqueTogether(
            name='devices',
            unique_together={('user', 'type')},
        ),
    ]
