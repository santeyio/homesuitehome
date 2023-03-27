import json
from channels.db import database_sync_to_async
from common.models import User

@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Exception('Could not authenticate user')

class ChannelsTokenAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        print('scope: ', json.dumps(scope, default=str))
        print('receive: ', receive)
        print('send: ', send)
        scope['user'] = await get_user(1) # REPLACE get_user(int(scope['query_string']))
        return await self.app(scope, receive, send)
