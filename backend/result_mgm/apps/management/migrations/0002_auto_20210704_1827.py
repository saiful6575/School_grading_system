# Generated by Django 3.2.4 on 2021-07-04 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgmclass',
            name='is_archived',
            field=models.BooleanField(default=False, verbose_name='Is Archived'),
        ),
        migrations.AddField(
            model_name='mgmsubject',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mgm_class_subject_ids', to='management.mgmclass'),
        ),
        migrations.AlterField(
            model_name='mgmclass',
            name='assigned_pupil',
            field=models.ManyToManyField(blank=True, null=True, related_name='pupil_class_ids', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mgmsubject',
            name='is_archived',
            field=models.BooleanField(default=False, verbose_name='Is Archived'),
        ),
    ]
