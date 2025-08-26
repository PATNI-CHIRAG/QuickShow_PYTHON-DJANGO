from django.urls import path
from . import views

urlpatterns = [
    # user site
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('movies/', views.movie_list, name='movie_list'),
    path('about/', views.about, name='about'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('checkout/<int:movie_id>/<str:show_date>/<str:show_time>/', views.checkout, name='checkout'),
    path('get_booked_seats/<int:movie_id>/<str:show_date>/<str:show_time>/', views.get_booked_seats, name='get_booked_seats'),
    path('booking_history/', views.booking_history, name='booking_history'),

    # Admin site
    path('deashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('deashboard/movie/add/', views.add_movie, name='add_movie'),
    path('deashboard/movie/edit/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('deashboard/movie/delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('deashboard/movie/<int:movie_id>/add_show/', views.add_show, name='add_show'),
    path('deashboard/show/edit/<int:show_id>/', views.edit_show, name='edit_show'),
    path('deashboard/show/delete/<int:show_id>/', views.delete_show, name='delete_show'),
    path('deashboard/all_users/', views.all_users, name='all_users'),
    path('deashboard/user/<int:user_id>/bookings/', views.user_bookings, name='user_bookings'),
]