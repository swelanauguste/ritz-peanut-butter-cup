from django.core.management.base import BaseCommand
from ...models import WeekPlan

class Command(BaseCommand):
    help = "Add a predefined list of weeks to the WeekPlan model"

    def handle(self, *args, **kwargs):
        WEEK_LIST = ["week1", "week2", "week3", "week4"]
        
        for week_no in WEEK_LIST:
            week, created = WeekPlan.objects.get_or_create(week=week_no)
            
            if created:
                self.stdout.write(self.style.SUCCESS(f"Week {week_no} added"))
            else:
                self.stdout.write(self.style.WARNING(f"Week {week_no} already exists"))
