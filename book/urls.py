from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('service/<int:service_id>/', views.service_details, name='service_details'),  
    path('service/<int:service_id>/book/', views.book_service, name='book_service'), 
    path('booking/<int:booking_id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),  # Booking Confirmation
    path('dashboard/', views.user_dashboard, name='user_dashboard'),  
    path('support/', views.support_page, name='support_page'),  
    path('register/', views.register, name='register'),  
    path('login/', views.login_view, name='login'),  
    path('logout/', views.user_logout, name='logout'), 
    path('blogs/', views.blog_list, name='blog_list'),  
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),  
    path('blogs/create/', views.create_blog, name='create_blog'), 
]
