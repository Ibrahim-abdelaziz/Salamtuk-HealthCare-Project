from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Doctor', views.DoctorView)
router.register('appoientment', views.ApooientmentView)
router.register('paitent', views.PaitentView)
router.register('Booking', views.BookingView)
router.register('Comments', views.CommentsView)
router.register('Attendance', views.AttendanceView)
router.register('Payment', views.PaymentView)


urlpatterns = [
    path('', include(router.urls)),
    path('', views.DoctorView),
    path('appoientment/', views.ApooientmentView),
    path('paitent/', views.PaitentView),
    path('comment/', views.CommentsView),
    path('book/', views.BookingView),
    #path('book/<int:pk>/', views.DoctorView,name="detail"),
    #path('Doctor/<int:pk>/', views.DoctorView,name="detail"),
]