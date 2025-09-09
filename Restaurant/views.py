from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth.models import User

from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """
    Read for everyone; write for authenticated users.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class BookingViewSet(viewsets.ModelViewSet):
    """
    Auth required for everything.
    """    
    queryset = Booking.objects.all().order_by('id')
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
    
class UserViewSet(generics.ListCreateAPIView):    
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


from django.shortcuts import render
from datetime import datetime
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required

from .forms import BookingForm


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')


def reservations(request):
    date_str = request.GET.get('date')
    if date_str:
        qs = Booking.objects.filter(reservation_date=date_str)
    else:
        qs = Booking.objects.all().order_by('-reservation_date', 'reservation_slot')

    data = list(qs.values('id', 'name', 'reservation_date', 'reservation_slot'))
    return render(request, 'bookings.html', {'bookings': json.dumps(data, default=str)})

# @login_required
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
# @login_required
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(
            reservation_date=data['reservation_date']
            ).filter(
            reservation_slot=data['reservation_slot']
            ).exists()
        if exist == False:
            booking = Booking(
                name=data.get('name') or data.get('first_name'),
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
                )
            booking.save()
        else :
            return HttpResponse("{'error':1}", content_type='application/json')

    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)
    return HttpResponse(booking_json, content_type='application/json')