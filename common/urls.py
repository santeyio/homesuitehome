from django.urls import include, path
from rest_framework import routers

from knox import views as knox_views
from .views import LoginView, HouseholdViewSet

router = routers.DefaultRouter()
router.register('households', HouseholdViewSet)

urlpatterns = [
    path('auth/', include([
        path('login/', LoginView.as_view(), name='knox_login'),
        path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
        path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    ])),
]
