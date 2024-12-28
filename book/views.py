from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Blog, Service, Booking, FAQ, ContactInfo
from .forms import BlogForm, UserRegistrationForm, UserLoginForm
import random
import string

def is_admin(user):
    return user.is_superuser  

# Home Page
@login_required
def home(request):
    services = Service.objects.all()  
    return render(request, 'book/home.html', {'services': services})

# Service Details
@login_required
def service_details(request, service_id):
    service = get_object_or_404(Service, id=service_id) 
    return render(request, 'book/service_details.html', {'service': service})

# Booking a Service
@login_required
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)  
    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')
        reference_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))  # Generating reference number
        booking = Booking.objects.create(
            user=request.user,
            service=service,
            booking_date=booking_date,
            reference_number=reference_number
        )
        messages.success(request, "Your booking was successful!")
        return redirect('booking_confirmation', booking_id=booking.id)
    return render(request, 'book/book_service.html', {'service': service})

# Booking Confirmation
@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id) 
    return render(request, 'book/booking_confirmation.html', {'booking': booking})

# User Dashboard
@login_required
def user_dashboard(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')  
    return render(request, 'book/dashboard.html', {'bookings': bookings})


@login_required
def support_page(request):
    faqs = FAQ.objects.all()  
    contact_info = ContactInfo.objects.all()  
    return render(request, 'book/support.html', {'faqs': faqs, 'contact_info': contact_info})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'book/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid login details.")
    else:
        form = UserLoginForm()
    return render(request, 'book/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at') 
    return render(request, 'book/blog_list.html', {'blogs': blogs})


@user_passes_test(is_admin)
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog post created successfully.")
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'book/create_blog.html', {'form': form})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id) 
    return render(request, 'book/blog_detail.html', {'blog': blog})