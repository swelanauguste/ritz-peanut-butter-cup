# Generated by Django 5.1 on 2024-08-31 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0014_remove_food_add_to_week_plan_delete_weekplan'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(max_length=5, null=True, unique=True)),
                ('created_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['week'],
            },
        ),
        migrations.AddField(
            model_name='food',
            name='add_to_week_plan',
            field=models.ManyToManyField(blank=True, to='foods.weekplan'),
        ),
    ]
