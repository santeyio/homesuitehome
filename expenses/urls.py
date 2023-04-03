from django.urls import include, path
from rest_framework import routers

from .views import ExpenditureViewSet, ExpenditureCategoryViewSet, BeneficiaryViewSet

router = routers.DefaultRouter()
router.register('expenditure', ExpenditureViewSet)
router.register('category', ExpenditureCategoryViewSet)
router.register('beneficiary', BeneficiaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
