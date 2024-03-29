from django.urls import include, path
from rest_framework import routers

from knox import views as knox_views
from . import views

router = routers.DefaultRouter()
router.register('households', views.HouseholdViewSet)

urlpatterns = [
    path('auth/', include([
        path('login/', views.LoginView.as_view(), name='knox_login'),
        path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
        path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
        path('check/', views.check_if_logged_in, name='check_if_logged_in'),
    ])),
    path('self/', views.get_self, name='get_self'),
]
