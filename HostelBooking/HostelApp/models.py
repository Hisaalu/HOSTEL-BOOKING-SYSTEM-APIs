from django.db import models

# Create your models here!.

class Hostel(models.Model):
    hostel_name = models.CharField(max_length=100, default='Olympia Hostel')

    def __str__(self):
        return self.hostel_name


class Room(models.Model):
    room_no = models.CharField(max_length=50)
    CATEGORY_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Tripple', 'Tripple'),
        # Add more categories if needed
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_no
    
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        # Add more statuses if needed
    ]
    booker = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    booked_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    # Other booking attributes...

    @property
    def booked_hostel(self):
        return f"{self.booked_room.hostel} - Room {self.booked_room.room_no}" if self.booked_room else "N/A"
    
    def __str__(self):
        return self.booker