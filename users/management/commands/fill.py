from django.core.management import BaseCommand

from catalog.models import Product, Category
import json

from config.settings import BASE_DIR

FIXTURES_BASE_DIR = BASE_DIR.joinpath('fixtures')


class Command(BaseCommand):

    @staticmethod
    def _load_fixtures(fixture_file_name: str):
        fixture_path = FIXTURES_BASE_DIR.joinpath(fixture_file_name)
        with fixture_path.open(encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def json_load_categories():
        return Command._load_fixtures('categories.json')

    @staticmethod
    def json_load_products():
        return Command._load_fixtures('products.json')

    def handle(self, *args, **options):
        categories_for_create = []
        product_for_create = []
        Category.objects.all().delete()
        Product.objects.all().delete()
        for category in Command.json_load_categories():
            categories_for_create.append(
                Category(pk=category['pk'],
                         name=category['fields']['name'],
                         description=category['fields']['description'])
            )

        Category.objects.bulk_create(categories_for_create)
        for product in Command.json_load_products():
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'])
            )
        Product.objects.bulk_create(product_for_create)
