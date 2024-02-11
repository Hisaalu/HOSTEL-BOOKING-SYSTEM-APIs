from .models import Room
from .models import Booking
from rest_framework import serializers

class Room_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
       
class Booking_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


#