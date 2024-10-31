from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import Car, CarInventory
from cars.gemini_integration import get_car_AI_bio


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        AI_bio = get_car_AI_bio(
            instance.brand, instance.model, instance.model_year
        )
        instance.bio = AI_bio


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
