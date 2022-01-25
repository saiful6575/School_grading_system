# Generated by Django 3.2.4 on 2021-06-20 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import result_mgm.apps.management.models.mgm_class
import result_mgm.apps.management.models.mgm_subject


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MgmSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Name')),
                ('unique_name', models.CharField(blank=True, default=result_mgm.apps.management.models.mgm_subject.create_new_ref_number, editable=False, max_length=20, unique=True, verbose_name='Unique Name')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Is Active')),
                ('assigned_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_teacher_ids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MgmTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Name')),
                ('test_date', models.DateField(blank=True, null=True, verbose_name='Test Date')),
                ('subject_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subject_test_ids', to='management.mgmsubject')),
            ],
        ),
        migrations.CreateModel(
            name='MgmTestParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Grade')),
                ('pupil_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pupil_test_ids', to=settings.AUTH_USER_MODEL)),
                ('test_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_participant_ids', to='management.mgmtest')),
            ],
        ),
        migrations.CreateModel(
            name='MgmClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Name')),
                ('unique_name', models.CharField(blank=True, default=result_mgm.apps.management.models.mgm_class.create_new_ref_number, editable=False, max_length=20, unique=True, verbose_name='Unique Name')),
                ('assigned_pupil', models.ManyToManyField(related_name='pupil_class_ids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
