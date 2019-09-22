from .models import Doctor, Booking, Comments, Appoientment, Paitent, Payment, Attendance
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField

post_detail = HyperlinkedIdentityField(
    view_name="detail",
    lookup_field="id",
)

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

class AppoientmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appoientment
        fields = "__all__"

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paitent
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    Doctor = PatientSerializer(many=True, read_only=True)
    class Meta:
        model = Booking
        fields = "__all__"

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

