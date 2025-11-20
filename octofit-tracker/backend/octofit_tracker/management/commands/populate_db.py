from django.core.management.base import BaseCommand
from core.models import Example
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete old data
        Example.objects.all().delete()
        User = get_user_model()
        User.objects.exclude(is_superuser=True).delete()

        # Insert test data: Superheroes, teams, etc.
        marvel_heroes = ['Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow']
        dc_heroes = ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman']

        for name in marvel_heroes:
            Example.objects.create(name=f"Marvel: {name}")
        for name in dc_heroes:
            Example.objects.create(name=f"DC: {name}")

        self.stdout.write(self.style.SUCCESS('Test data populated: Example superheroes created.'))
