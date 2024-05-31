import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import Expenditure, ExpenditureCategory
from .serializers import ExpenditureSerializer, ExpenditureCategorySerializer

@receiver(post_save, sender=Expenditure)
def expenditure_post_save(sender, instance, *args, **kwargs):
    household_id = instance.household.id
    channel_layer = get_channel_layer()
    group_name = f'expenditure_{household_id}'
    serializer = ExpenditureSerializer(instance)
    async_to_sync(channel_layer.group_send)(group_name, {
        'type': 'expenditure.added',
        'content': serializer.data,
    })

@receiver(post_save, sender=ExpenditureCategory)
def expenditure_category_post_save(sender, instance, *args, **kwargs):
    household_id = instance.household.id
    channel_layer = get_channel_layer()
    group_name = f'expenditure_category_{household_id}'
    serializer = ExpenditureCategorySerializer(instance)
    async_to_sync(channel_layer.group_send)(group_name, {
        'type': 'expenditure_category.added',
        'content': serializer.data,
    })
