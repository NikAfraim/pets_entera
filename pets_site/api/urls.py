"""
Содержит маршруты для API.
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('users', views.UserViewSet, basename='users')
router.register('types', views.TypeViewSet, basename='types')
router.register('pets', views.PetViewSet, basename='pets')

urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.jwt')),
]
