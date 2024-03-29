# Generated by Django 3.2 on 2022-10-20 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('COMPLETED', 'Completed'), ('STARTED', 'Started'), ('FAILED', 'Failed')], default='CREATED', max_length=256)),
                ('type', models.CharField(max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SEMGSensorData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('rightc4_paraspinal', models.FloatField(blank=True, null=True)),
                ('leftc4_paraspinal', models.FloatField(blank=True, null=True)),
                ('right_multifidus', models.FloatField(blank=True, null=True)),
                ('left_multifidus', models.FloatField(blank=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infra.session', verbose_name='Session')),
            ],
        ),
        migrations.CreateModel(
            name='IRSensorData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infra.session', verbose_name='Session')),
            ],
        ),
        migrations.CreateModel(
            name='InertialSensorData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('l5s1_lateral', models.FloatField(blank=True, null=True)),
                ('l5s1_axial', models.FloatField(blank=True, null=True)),
                ('l5s1_flexion', models.FloatField(blank=True, null=True)),
                ('l4l3_lateral', models.FloatField(blank=True, null=True)),
                ('l4l3_axial', models.FloatField(blank=True, null=True)),
                ('l4l3_flexion', models.FloatField(blank=True, null=True)),
                ('l1t12_lateral', models.FloatField(blank=True, null=True)),
                ('l1t12_axial', models.FloatField(blank=True, null=True)),
                ('l1t12_flexion', models.FloatField(blank=True, null=True)),
                ('t9t8_lateral', models.FloatField(blank=True, null=True)),
                ('t9t8_axial', models.FloatField(blank=True, null=True)),
                ('t9t8_flexion', models.FloatField(blank=True, null=True)),
                ('t1c7_lateral', models.FloatField(blank=True, null=True)),
                ('t1c7_axial', models.FloatField(blank=True, null=True)),
                ('t1c7_flexion', models.FloatField(blank=True, null=True)),
                ('c1head_lateral', models.FloatField(blank=True, null=True)),
                ('c1head_axial', models.FloatField(blank=True, null=True)),
                ('c1head_flexion', models.FloatField(blank=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infra.session', verbose_name='Session')),
            ],
        ),
    ]
