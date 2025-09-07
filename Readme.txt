SUPERUSER
user: admin_01
email: admin.01@lemon.com
password: batman@321


USER
user: user_01
email: user.01@lemon.com
password: batgirl@321


http://127.0.0.1:8000

Restaurant HTML
/restaurant/   -> home
/restaurant/about/   ->about
/restaurant/menu/   -> menu
/restaurant/book/   -> book
/restaurant/reservations/   -> reservations

Top-level
/auth/users/   -> POST, create user (USER REGISTRATION)
/auth/token/login/   -> POST, creates token (use on protected DRF views)
/auth/users/me/   -> GET, 
/auth/token/logout/   -> POST, destroys token
/admin/   -> admin

Restaurant API
/restaurant/api/menu-items/   -> menu-tems
/restaurant/api/menu-items/1/   -> menu_item
/restaurant/api/bookings/   -> booking-list
/restaurant/api/bookings/1/   -> booking-detail

___

Bookings API: IsAuthenticated -> requires token or session
MenuItem API: IsAuthenticatedOrReadOnly -> anyone can view menu, only auth can change
___