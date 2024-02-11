from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Room_Serializer, Booking_Serializer
from .models import Room, Booking
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

#create your views here
    
class Room_View(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = Room_Serializer


    def retrieve_by_id(self, request, pk=None):
        room = get_object_or_404(Room, pk=pk)
        serializer = self.get_serializer(room)
        return Response(serializer.data)
    
class Booking_View(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = Booking_Serializer


    def retrieve_by_id(self, request, pk=None):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = self.get_serializer(booking)
        return Response(serializer.data)    