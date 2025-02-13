from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request,"flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    # pf - primary key
    try:
        flight = Flight.objects.get(pk=flight_id)
        return render(request,"flights/flight.html", {
        "flight": flight,
        # we can do it as we set related name "passengers" 
        "passengers": flight.passengers.all(),
        # so we exclude passengers whose flight is current flight, and get me all of them
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })
    except Flight.DoesNotExist:
        return render(request,"flights/error.html")
    
def book(request, flight_id):
   if request.method == "POST":
       flight = Flight.objects.get(pk=flight_id)
    # It means that info about the flight will be passed via POST(submitting the form) from passenger field   
    # getting the entry of our db for the user that we get from that "passenger" form submission
       passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
       passenger.flights.add(flight)
       return HttpResponseRedirect(reverse("flight",args=(flight.id,)))
    