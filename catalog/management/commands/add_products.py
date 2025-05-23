from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data drom fixture'))