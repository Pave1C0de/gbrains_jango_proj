from django.core.management import BaseCommand

from mainapp.models import Category, Product

from django.conf import settings

from authapp.models import ShopUser

import json

class Command(BaseCommand):
    @staticmethod
    def _load_data_from_file(file_name):
        with open(f'{settings.BASE_DIR}/mainapp/json/{file_name}.json') as json_file:
            #json_string = json_file.read()
            #return json.loads(json_string)
            return json.load(json_file)

    def handle(self, *args, **options):
        Category.objects.all().delete()

        categories_list = self._load_data_from_file("categories")
        print(categories_list)

        categories_batch = []
        for cat in categories_list:
            categories_batch.append(
                Category(
                name=cat.get('name'),
                description=cat.get('description')
            )  )
        Category.objects.bulk_create(categories_batch)

        Product.objects.all().delete()
        products_list = self._load_data_from_file('products')

        for prod in products_list:
            print(prod)
            _cat = Category.objects.get(name=prod.get('category'))
            prod['category'] = _cat

            Product.objects.create(**prod)

        shop_user = ShopUser.objects.create_superuser(username='django', email='django@bg.local', age=31)
        shop_user.set_password('geekbrains')
        shop_user.save()