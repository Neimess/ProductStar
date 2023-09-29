from rest_framework.routers import DefaultRouter

from api.views import UserModelViewSet, BookingModelViewSet, HotelModelViewSet, RoomModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('bookings', BookingModelViewSet)
router.register('hotels', HotelModelViewSet)
router.register('rooms', RoomModelViewSet)

urlpatterns = [
    
]

urlpatterns.extend(router.urls)