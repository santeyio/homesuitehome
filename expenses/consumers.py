import json
from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync

from .models import Expenditure, ExpenditureCategory
from common.models import Household
from common.decorators import require_auth


class ExpenditureConsumer(JsonWebsocketConsumer):
    def connect(self):
        # note that we don't have access to the user in connect, the user is authenticated
        # after they have connected with the require_auth decorator.
        household_id = self.scope['url_route']['kwargs']['household_id']
        group_name = f'expenditure_{household_id}'
        async_to_sync(self.channel_layer.group_add)(group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        household_id = self.scope['url_route']['kwargs']['household_id']
        group_name = f'expenditure_{household_id}'
        async_to_sync(self.channel_layer.group_discard)(group_name, self.channel_name)

    @require_auth
    def receive_json(self, content):
        self.send_json(content)

    def expenditure_added(self, event):
        self.send_json(event['content'])

class ExpenditureCategoryConsumer(JsonWebsocketConsumer):
    def connect(self):
        # note that we don't have access to the user in connect, the user is authenticated
        # after they have connected with the require_auth decorator.
        household_id = self.scope['url_route']['kwargs']['household_id']
        group_name = f'expenditure_category_{household_id}'
        async_to_sync(self.channel_layer.group_add)(group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        household_id = self.scope['url_route']['kwargs']['household_id']
        group_name = f'expenditure_category_{household_id}'
        async_to_sync(self.channel_layer.group_discard)(group_name, self.channel_name)

    @require_auth
    def receive_json(self, content):
        self.send_json(content)

    def expenditure_added(self, event):
        self.send_json(event['content'])
