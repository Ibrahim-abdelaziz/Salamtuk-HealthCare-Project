from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_auth.registration.views import VerifyEmailView

from .views import ProfileApiView
from rest_auth.views import (
                            LoginView, PasswordResetView,
                            PasswordResetConfirmView, PasswordChangeView,
                            LogoutView
                            )
#from rest_auth.registration.views import RegisterView, VerifyEmailView
#from accounts.views import ProfileApiView

urlpatterns = [
    path('profile/', ProfileApiView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/<str:uidb64>/<str:token>/',
            PasswordResetConfirmView.as_view(),
            name='rest_password_reset_confirm'),

    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),

    path('account-confirm-email/sent/', TemplateView.as_view(), name='account_confirm_email'),
    path('account-confirm-email/<str:key>', VerifyEmailView.as_view(), name='rest_verify_email'),
    #path('profile/<int:pk>/', ProfileApiView.as_view()),
    #path('user/<str:username>/', views.UserDetailView.as_view()),
    #path('api-auth/',include('rest_framework.urls')),
    #path('api/auth/token/', TokenObtainPairView.as_view()),
    #path('api/auth/token/refresh/', TokenRefreshView.as_view()),
]