from django.core.management.base import BaseCommand
from app_goods.models import Shop, Item, ItemInstance
from random import choice, randint

NUMBER_OF_SHOPS = 2
NUMBER_OF_ITEMS = 5
NUMBER_OF_ITEM_INSTANCES = 20


class Command(BaseCommand):
    help = 'добавление записей в таблицу ItemInstance'

    def handle(self, *args, **kwargs):
        shops = []
        for i_shop in range(NUMBER_OF_SHOPS):
            shop = Shop(name=f'магазин_{i_shop}')
            shops.append(shop)
        Shop.objects.bulk_create(shops)
        items = []
        for i_item in range(NUMBER_OF_ITEMS):
            item = Item(shop=choice(Shop.objects.all()), name=f'товар_{i_item}',
                        description=f'описание товара_{i_item}', price=randint(10, 100), number_on_sale=5)
            items.append(item)
        Item.objects.bulk_create(items)
        item_instances = []
        for i_item_instances in range(NUMBER_OF_ITEM_INSTANCES):
            item_instance = ItemInstance(item=choice(Item.objects.all()))
            item_instances.append(item_instance)
        ItemInstance.objects.bulk_create(item_instances)
        self.stdout.write(f'добавили товаров:{NUMBER_OF_ITEMS}, экземпляров товаров:{NUMBER_OF_ITEM_INSTANCES}')
