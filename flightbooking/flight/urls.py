from django.urls import path
from . import views

namespace = 'flight'
urlpatterns = [
    path('user/signup/',views.signup,name='signup'),
    path('flight/list/',views.flightList,name='FlightList'),
    path('flight/book/<int:flight_id>', views.bookings, name ='Booking'),
    path('bookings/list/', views.bookingList, name='BookingList'),
    path('',views.user_login, name='user_login'),
    path('search-flights/', views.search_flights, name='search_flights'),
    path('selection/',views.selection,name='selection'),
    path('logout/',views.user_logout,name='user_logout')

]
