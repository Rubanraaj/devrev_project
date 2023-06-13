from django.urls import path
from . import views

namespace = 'flight'
urlpatterns = [
    path('user/signup/',views.home,name='signup'),
    path('flight/list/',views.flightList,name='FlightList'),
    path('flight/book/<int:flight_id>', views.bookings, name ='Booking'),
    path('bookings/list/', views.bookingList, name='BookingList'),
    path('login/',views.login, name='login')

]
