from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Movie , Show ,Booking
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django import template
import datetime
import json


def home(request):
    # return render(request, 'user/home.html')
    movies = Movie.objects.all()  # ✅ Only first 4 movies
    return render(request, 'user/home.html', {'movies': movies})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login Successful!')
            next_url = request.GET.get('next') or request.POST.get('next')
            return redirect(next_url or 'home')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect(request.GET.get('next') or 'home')
    return redirect('home')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Registration Successful!')
            next_url = request.GET.get('next') or request.POST.get('next')
            return redirect(next_url or 'home')
        else:
            messages.error(request, 'User already exists!')
            return redirect(request.GET.get('next') or 'home')

    return redirect('home')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def about(request):
    return render(request,'user/about.html')

def movie_list(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(title__icontains=search_term) | Movie.objects.filter(genre__icontains=search_term)
        if (len(movies)==0):
            movies = Movie.objects.all().order_by('-id') 
    else:
        movies = Movie.objects.all().order_by('-id')  
    return render(request, 'user/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    shows = Show.objects.filter(movie=movie)
    bookings = Booking.objects.filter(movie=movie)

    booked = []
    for b in bookings:
        booked += b.selected_seats.split(',')

    return render(request, 'user/movie_detail.html', {
        'movie': movie,
        'shows': shows,
        'booked_seats': json.dumps(booked)
    })


def get_booked_seats(request, movie_id, show_date, show_time):
    bookings = Booking.objects.filter(
        movie_id=movie_id,
        show_date=show_date,
        show_time=show_time
    )

    booked_seats = []
    for booking in bookings:
        booked_seats.extend(booking.selected_seats.split(','))

    return JsonResponse({'booked_seats': booked_seats})

@csrf_exempt
def checkout(request, movie_id, show_date, show_time):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Login required')
            return redirect('login')

        selected_seats = request.POST.get('selected_seats')
        payment_method = request.POST.get('payment_method')
        movie = get_object_or_404(Movie, id=movie_id)

        # Convert string to date & time
        try:
            show_date_obj = datetime.datetime.strptime(show_date, "%Y-%m-%d").date()
            show_time_obj = datetime.datetime.strptime(show_time, "%H:%M:%S").time()
        except ValueError:
            return HttpResponseBadRequest("Invalid date/time format")

        # Check for already booked seats
        existing = Booking.objects.filter(movie=movie, show_date=show_date_obj, show_time=show_time_obj)
        booked_seats = []
        for b in existing:
            booked_seats.extend(b.selected_seats.split(','))

        selected_list = selected_seats.split(',')
            
        try:
            total_seats = len(selected_list)
            total_price = float(movie.price) * total_seats
        except:
            return HttpResponseBadRequest("Invalid price or seat count")

        # Save booking
        Booking.objects.create(
            user=request.user,
            movie=movie,
            show_date=show_date_obj,
            show_time=show_time_obj,
            price=total_price,
            selected_seats=selected_seats,
            payment_method=payment_method,
        )
        messages.success(request, 'Booking successful!')
        return JsonResponse({'status': 'success'})

    messages.error(request, 'Invalid request method!')
    return JsonResponse({'status': 'error'})

def booking_history(request,):
    if not request.user.is_authenticated:
        messages.error(request, 'Login required to view booking history')
        return redirect('login')
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'user/booking_history.html', {'bookings': bookings ,})

def is_superuser(user):
    return user.is_superuser

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from .forms import MovieForm ,ShowForm 

@user_passes_test(is_superuser)
def admin_dashboard(request):
    movies = Movie.objects.all().order_by('-id')
    return render(request, 'admin/admin_dashboard.html', {'movies': movies})


# @login_required
@user_passes_test(is_superuser)
def add_movie(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, request.FILES)
        show_form = ShowForm(request.POST)
        if movie_form.is_valid() and show_form.is_valid():
            movie = movie_form.save()
            show = show_form.save(commit=False)
            show.movie = movie
            show.save()
            messages.success(request, "Movie Added successfully.")
            return redirect('admin_dashboard')
    else:
        movie_form = MovieForm()
        show_form = ShowForm()
    
    return render(request, 'admin/add_movie.html', {
        'movie_form': movie_form,
        'show_form': show_form,
        'action': 'Add'
    })

@user_passes_test(is_superuser)
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    shows = Show.objects.filter(movie=movie)  # Multiple shows

    if request.method == 'POST':
        movie_form = MovieForm(request.POST, request.FILES, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            messages.success(request, "Movie updated successfully.")
            return redirect('admin_dashboard')
    else:
        movie_form = MovieForm(instance=movie)

    return render(request, 'admin/edit_movie.html', {
        'movie_form': movie_form,
        'movie': movie,
        'shows': shows,
    })


@user_passes_test(is_superuser)
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    messages.success(request, 'Movie deleted successfully!')
    return redirect('admin_dashboard')

def add_show(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        show_form = ShowForm(request.POST)
        if show_form.is_valid():
            show = show_form.save(commit=False)
            show.movie = movie
            show.save()
            messages.success(request, "Show added successfully.")
            return redirect('admin_dashboard')
    else:
        show_form = ShowForm()

    return render(request, 'admin/add_show.html', {
        'movie': movie,
        'show_form': show_form,
    })


@user_passes_test(is_superuser)
def edit_show(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    if request.method == 'POST':
        show_form = ShowForm(request.POST, instance=show)
        if show_form.is_valid():
            show_form.save()
            messages.success(request, "Show updated successfully.")
            return redirect('edit_movie', movie_id=show.movie.id)
    else:
        show_form = ShowForm(instance=show)

    return render(request, 'admin/edit_show.html', {
        'show_form': show_form,
        'movie': show.movie,
        'show': show,
    })

@user_passes_test(is_superuser)
def delete_show(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    movie_id = show.movie.id
    show.delete()
    messages.success(request, "Show deleted successfully.")
    return redirect('edit_movie', movie_id=movie_id)

@user_passes_test(is_superuser)
def all_users(request):
    users = User.objects.filter(is_superuser=False).order_by('username')
    return render(request, 'admin/all_users.html', {'users': users})


@user_passes_test(is_superuser)
def user_bookings(request, user_id):
    user = User.objects.get(id=user_id)
    bookings = Booking.objects.filter(user=user).order_by('-created_at')
    return render(request, 'admin/user_bookings.html', {'user': user, 'bookings': bookings})




# def movie_detail(request, movie_id):
#     movie = Movie.objects.get(id=movie_id)
#     shows = Show.objects.filter(movie=movie).order_by('date', 'time')
#     return render(request, 'user/movie_detail.html', {'movie': movie, 'shows': shows})
