import os
import json
from django.db.models.signals import pre_save, post_save, pre_delete
from config.settings import BASE_DIR
from app.models import Product
from django.dispatch import receiver


@receiver(post_save, sender=Product)
def product_save(sender, instance, created, **kwargs):
    if created:
        print(f'{instance.name} is created!')
        print(kwargs)
    else:
        print('Product Updated')


