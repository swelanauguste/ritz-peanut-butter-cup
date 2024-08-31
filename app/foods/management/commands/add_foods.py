import csv
from django.core.management.base import BaseCommand
from ...models import Food, Tag, Group, Family

class Command(BaseCommand):
    help = 'Load food data from a CSV file'

    def handle(self, *args, **kwargs):
        with open('static/docs/foods.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create or get the tags
                tags = []
                for tag_name in [row['NAME'], row['FAMILY'], row['GROUP'], row['FAMILY EASY NAME']]:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    tags.append(tag)

                # Create or update the Food object
                food, created = Food.objects.update_or_create(
                    name=row['NAME'],
                    defaults={
                        'family': Family.objects.get(name=row['FAMILY'].lower().strip()),
                        'group': Group.objects.get(name=row['GROUP'].lower().strip()),
                    }
                )

                # Add the tags to the Food object
                food.tags.set(tags)
                food.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from CSV'))
