Hi,
Steps:
1. Clone the repository from GitHub.
2. Step into the cloned repository.
3. run: pipenv install  (Installs the dependencies that are in the Pipfile)
4. run: pipenv shell (Activates the virtual environment)
5. Update the USER and PASSWORD of the mysql in settings.py
6. run: python manage.py runserver (Continue from there)


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


Practice Peer-graded Assignment: Little Lemon Web Application

Project Title
Back-end developer capstone project

https://github.com/Hassan-elSayyed/LargeLemon

