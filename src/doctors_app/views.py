from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from Notifications.utils import push_notifications
from .models import Doctor, Booking, Comments, Appoientment, Paitent, Payment, Attendance
from .serializers import DoctorSerializer, BookingSerializer, CommentsSerializer, AppoientmentSerializer, \
    PatientSerializer, PaymentSerializer, AttendanceSerializer
from rest_framework import viewsets
from rest_framework.filters import (SearchFilter,
                                    OrderingFilter, )

# from rest_framework.response import Response
# from rest_framework import status

class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [SearchFilter, OrderingFilter]

class ApooientmentView(viewsets.ModelViewSet):
    queryset = Appoientment.objects.all()
    serializer_class = AppoientmentSerializer

class PaitentView(viewsets.ModelViewSet):
    queryset = Paitent.objects.all()
    serializer_class = PatientSerializer

class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            push_notifications(title="title", body="body", user=self.request.user)
            return Response(serializer.data)



class CommentsView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class AttendanceView(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer









