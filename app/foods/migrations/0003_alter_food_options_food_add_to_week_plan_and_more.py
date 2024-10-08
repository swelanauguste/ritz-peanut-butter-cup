# Generated by Django 5.1 on 2024-08-18 00:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_food_created_by_alter_food_family_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='food',
            name='add_to_week_plan',
            field=models.CharField(choices=[('WEEK1', 'Week 1'), ('WEEK2', 'Week 2'), ('WEEK3', 'Week 3'), ('WEEK4', 'Week 4')], default='WEEK1', max_length=5),
        ),
        migrations.AlterField(
            model_name='food',
            name='created_by',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
