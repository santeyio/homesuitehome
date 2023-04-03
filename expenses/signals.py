import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import Expenditure
from .serializers import ExpenditureSerializer

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
