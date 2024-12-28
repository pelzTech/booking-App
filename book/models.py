from django.db import models
from django.contrib.auth.models import User
import uuid


class Service(models.Model):
    SERVICE_TYPES = [
        ('Hotel', 'Hotel'),
        ('Accommodation', 'Accommodation'),
        ('Event', 'Event'),
        ('Travel', 'Travel'),  
    ]
    name = models.CharField(max_length=100)
    service_type = models.CharField(choices=SERVICE_TYPES, max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)  

    def __str__(self):
        return f"{self.name} ({self.service_type})"

    def formatted_price(self):
        """Returns the price with a currency symbol."""
        return f"${self.price_per_unit:,.2f}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    booking_date = models.DateField()
    reference_number = models.CharField(max_length=10, unique=True, default=uuid.uuid4().hex[:10].upper())  # Generates unique reference
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reference_number} - {self.service.name}"


class Payment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'), 
    ]
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    transaction_id = models.CharField(max_length=50, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.status}"

    def formatted_amount(self):
        """Returns the payment amount with a currency symbol."""
        return f"${self.amount:,.2f}"


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f"FAQ: {self.question}"


class ContactInfo(models.Model):
    platform_name = models.CharField(max_length=50)
    link = models.URLField()
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)  

    def __str__(self):
        return f"{self.platform_name} Contact"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
