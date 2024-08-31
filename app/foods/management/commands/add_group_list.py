import csv
from django.core.management.base import BaseCommand
from ...models import Group

class Command(BaseCommand):
    help = 'Load group data from a CSV file'

    def handle(self, *args, **kwargs):
        with open('static/docs/foods.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
              

                # Create or update the group object
                group, created = Group.objects.update_or_create(
                    name=row['GROUP'].lower().strip(),
                )
                group.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from CSV'))
