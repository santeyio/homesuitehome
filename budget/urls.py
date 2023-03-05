from django.urls import include, path
from rest_framework import routers

from .views import ExpenditureViewSet

router = routers.DefaultRouter()
router.register('expenditures', ExpenditureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
