from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/expenditure/<household_id>/', consumers.ExpenditureConsumer.as_asgi()),
    path('ws/expenditure-category/<household_id>/', consumers.ExpenditureCategoryConsumer.as_asgi()),
]
