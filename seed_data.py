import os
import django
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from flights.models import Flight
from tours.models import Tour

now = timezone.now()

# Create Past Flights (for Area Chart)
Flight.objects.create(
    airline="Biman Bangladesh",
    origin="Dhaka (DAC)",
    destination="Dubai (DXB)",
    departure_time=now - timedelta(days=2, hours=5),
    arrival_time=now - timedelta(days=2, hours=1),
    price=55000.00
)
Flight.objects.create(
    airline="Emirates",
    origin="Dhaka (DAC)",
    destination="London (LHR)",
    departure_time=now - timedelta(days=5, hours=2),
    arrival_time=now - timedelta(days=4, hours=20),
    price=95000.00
)
Flight.objects.create(
    airline="Qatar Airways",
    origin="Dhaka (DAC)",
    destination="Doha (DOH)",
    departure_time=now - timedelta(days=1, hours=8),
    arrival_time=now - timedelta(days=1, hours=3),
    price=62000.00
)

# Create Upcoming Flights
Flight.objects.create(
    airline="Singapore Airlines",
    origin="Dhaka (DAC)",
    destination="Singapore (SIN)",
    departure_time=now + timedelta(days=2, hours=10),
    arrival_time=now + timedelta(days=2, hours=14),
    price=45000.00
)
Flight.objects.create(
    airline="Saudi Airlines",
    origin="Dhaka (DAC)",
    destination="Jeddah (JED)",
    departure_time=now + timedelta(days=5, hours=6),
    arrival_time=now + timedelta(days=5, hours=12),
    price=85000.00
)
Flight.objects.create(
    airline="US-Bangla Airlines",
    origin="Dhaka (DAC)",
    destination="Kolkata (CCU)",
    departure_time=now + timedelta(days=1, hours=9),
    arrival_time=now + timedelta(days=1, hours=10),
    price=12000.00
)

# Create Tours with images if possible
# We can re-use the existing image path that was found in the DB, e.g., 'tours/Screenshot_20260812-081702.png'
Tour.objects.create(
    destination="Cox's Bazar Sea Beach",
    duration="3 Days 2 Nights",
    price=15000.00,
    inclusions="Hotel, Breakfast, Transport",
    image="tours/Screenshot_20260812-081702.png"
)
Tour.objects.create(
    destination="Sajek Valley Paradise",
    duration="2 Days 1 Night",
    price=8500.00,
    inclusions="Jeep, Cottage, Meals",
    image="tours/Screenshot_20260812-081702.png" 
)

print("Dummy data seeded successfully!")
