from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/expenditure/<household_id>/', consumers.ExpenditureConsumer.as_asgi()),
]
