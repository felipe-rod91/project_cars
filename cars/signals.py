from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print('Saving', instance, '...')


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print(instance, 'SAVED!')


@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print('Deleting', instance, '...')


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print(instance, 'DELETED!')
