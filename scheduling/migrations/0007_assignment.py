# Generated by Django 2.0.1 on 2018-01-15 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freegeek', '0003_roster'),
        ('scheduling', '0006_volunteershift'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('closed', models.BooleanField()),
                ('lock_version', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('call_status_type_id', models.IntegerField(blank=True, null=True)),
                ('attendance_type_id', models.IntegerField(blank=True, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='freegeek.Contact')),
                ('volunteer_shift', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scheduling.VolunteerShift')),
            ],
            options={
                'db_table': 'assignments',
            },
        ),
    ]