from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # HTML pages
    path('', views.home, name='home'), # {% url 'home' %}
    path('about/', views.about, name='about'), # {% url 'about' %}
    path('menu/', views.menu, name='menu'), # {% url 'menu' %}
    path('book/', views.book, name='book'), # {% url 'book' %}
    path('reservations/', views.reservations, name="reservations"), # {% url 'reservations' %}
    
    # JSON used by pages (book.html)
    path('bookings/', views.bookings, name='bookings'), # JSON feed used by the template
        
    # API (DRF, machine-consumed)
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/menu-items/', views.MenuItemsView.as_view(), name='menu-tems'),
    path('api/menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu_item'),
    path('api/bookings/', views.BookingsView.as_view(), name='booking-list'), # LIST/CREATE
    path('api/bookings/<int:pk>/', views.SingleBookingView.as_view(), name='booking-detail'),  # RETR/UPD/DEL

    path('users/', views.UserViewSet.as_view(), name='users'), # admin-only, for debugging
]


