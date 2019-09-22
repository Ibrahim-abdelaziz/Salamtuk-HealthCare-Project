from django.shortcuts import render
from . models import Profile
from . serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.exceptions import PermissionDenied, NotAcceptable, ValidationError
from rest_auth.views import (LoginView, PasswordResetView, PasswordResetConfirmView,
                                PasswordChangeView, LogoutView)
from django.contrib.auth.models import User

# Create your views here.

class ProfileApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        profile = Profile.objects.get(pk=pk)
        serializer = UserProfileSerializer(profile, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

