from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models import ApiUser, Room, Booking, Hotel
from api.serializers import UserSerializer, RoomSerializer, BookingSerializer, HotelSerializer
# Create your views here.


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ["post", "patch", "get"]
    serializer_class = UserSerializer
    
    # authentication_classes = []
    # permission_classes = []

class HotelModelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
    @action(detail=True)
    def rooms(self, request, pk=None):
        hotel = get_object_or_404(Hotel.objects.all(), id=pk)
        free_rooms = hotel.rooms.filter(bookings__isnull=True)
        return Response(
            RoomSerializer(free_rooms, many=True).data
        )
    
class RoomModelViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class BookingModelViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
