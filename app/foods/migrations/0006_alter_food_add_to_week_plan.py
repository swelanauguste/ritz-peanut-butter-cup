# Generated by Django 5.1 on 2024-08-18 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_tag_remove_food_tags_food_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='add_to_week_plan',
            field=models.CharField(blank=True, choices=[('WEEK1', 'Week 1'), ('WEEK2', 'Week 2'), ('WEEK3', 'Week 3'), ('WEEK4', 'Week 4')], max_length=5),
        ),
    ]
