# Generated by Django 5.1 on 2024-08-18 00:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='food',
            name='family',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='food',
            name='friendly_family_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
