import csv
from django.core.management.base import BaseCommand
from ...models import Family

class Command(BaseCommand):
    help = 'Load family data from a CSV file'

    def handle(self, *args, **kwargs):
        with open('static/docs/foods.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                # Create or update the family object
                family, created = Family.objects.update_or_create(
                    name=row['FAMILY'].lower().strip(),
                )
                family.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from CSV'))

