from django.contrib import admin
from django.urls import path, include
from Notifications import views
from .views import NotificationView
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet


router = DefaultRouter()
router.register('Notifications', views.NotificationView, basename='NotificationView')


urlpatterns = [
    path('', include(router.urls)),


]
