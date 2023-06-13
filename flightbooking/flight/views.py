from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import *
from .models import Flight, Booking
from django.shortcuts import redirect
from django.urls import reverse 
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

def home(request):
    form = UserSignUpForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(flightList)
    return render(request, 'layout.html', {'signupform':form} )
        
def flightList(request):
    flights = list(Flight.objects.all())
    return render(request, 'flights.html', context = {'flights_list':flights})

def bookings(request,flight_id):
    flight = Flight.objects.get(id = flight_id)
    user = User.objects.get(id = request.user.id)
    booking = Booking(user = user, flight = flight)
    booking.save()
    return redirect(bookingList)

def bookingList(request):
    bookings = list(Booking.objects.all())
    return render(request,'bookings.html', context= {'bookings_list':bookings} )

def login(request):
    if request.method == "POST":
        form = UserLoginForm(request)
    
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {email}.")
            return redirect(flightList)
        else:
            messages.error(request,"Invalid email or password.")
    form = UserLoginForm()
    return render(request=request, template_name="login.html", context={"login_form":form})