from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import Car, CarInventory


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Bio gerada automaticamente.'


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_price = Car.objects.aggregate(
        total_price = Sum('price')
    )['total_price']
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_price = cars_price
    )


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()    


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
