from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import *
from .models import Flight, Booking
from django.shortcuts import redirect
from django.urls import reverse 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 


def signup(request):
    form = UserSignUpForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully signed up. Please log in.')
            return redirect(user_login)
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

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {email}.")
                return redirect(selection)
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = UserLoginForm()
    return render(request=request, template_name="login.html", context={"login_form": form})
    
def search_flights(request):
    if request.method == 'GET':
        depart_date = request.GET.get('depart_date')
        depart_time = request.GET.get('depart_time')
        flights = Flight.objects.filter(depart_time__date=depart_date, depart_time__time=depart_time)
    else:
        flights = []

    return render(request, 'flight_search.html', {'flights': flights})

def selection(request):
    return render(request, 'selection.html')

def user_logout(request):
    logout(request)
    return redirect(user_login) 