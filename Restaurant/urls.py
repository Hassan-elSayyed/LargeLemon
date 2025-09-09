from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'menu-items', views.MenuItemViewSet, basename='menuitem')
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = [
    # HTML pages
    path('', views.home, name='home'), # {% url 'home' %}
    path('about/', views.about, name='about'), # {% url 'about' %}
    path('menu/', views.menu, name='menu'), # {% url 'menu' %}
    path('book/', views.book, name='book'), # {% url 'book' %}
    path('reservations/', views.reservations, name="reservations"), # {% url 'reservations' %}
    
    # Auth token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),    
    
    # DRF ViewSets
    path('', include(router.urls)),
    
    # JSON used by pages (book.html)
    path('bookings/', views.bookings, name='bookings'), # JSON feed used by the template

    path('users/', views.UserViewSet.as_view(), name='users'), # admin-only, for debugging
]


