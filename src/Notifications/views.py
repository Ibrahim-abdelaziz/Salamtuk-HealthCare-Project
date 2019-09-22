from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework import permissions
from .models import Notification
from rest_framework import viewsets
from .utils import push_notifications
from .serializers import NotificationSerializer


class NotificationView(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.AllowAny]




