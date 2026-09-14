from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
import calendar

# Import all actual models used by the system
from flights.models import Flight
from customers.models import Customer
from tours.models import Tour
from visas.models import Visa
from umrah.models import UmrahPackage
from deals.models import Deal

class DashboardStatsView(APIView):
    def get(self, request):
        time_filter = request.GET.get('time_filter', 'this_month')
        
        now = timezone.now()
        start_date = None
        end_date = None
        
        if time_filter == 'this_month':
            start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            # End of this month
            last_day = calendar.monthrange(now.year, now.month)[1]
            end_date = now.replace(day=last_day, hour=23, minute=59, second=59)
        elif time_filter == 'last_month':
            first_day_this_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            last_month_last_day = first_day_this_month - timedelta(days=1)
            start_date = last_month_last_day.replace(day=1)
            end_date = last_month_last_day.replace(hour=23, minute=59, second=59)
        elif time_filter == 'last_3_months':
            start_date = now - timedelta(days=90)
            end_date = now
            
        flight_qs = Flight.objects.all()
        customer_qs = Customer.objects.all()
        
        if start_date and end_date:
            flight_qs = flight_qs.filter(departure_time__gte=start_date, departure_time__lte=end_date)
            customer_qs = customer_qs.filter(joined_date__gte=start_date.date(), joined_date__lte=end_date.date())

        # Tours, Visas, Umrah don't have date fields so we just take counts
        tour_qs = Tour.objects.all()
        visa_qs = Visa.objects.all()
        umrah_qs = UmrahPackage.objects.all()
        deal_qs = Deal.objects.all()

        # 1. Top Stats
        total_bookings = flight_qs.count() + tour_qs.count() + visa_qs.count() + umrah_qs.count() + deal_qs.count()
        
        top_stats = [
            {'label': 'মোট বুকিং', 'value': str(total_bookings), 'inc': '০%', 'icon': 'Briefcase', 'iconBg': 'bg-blue-100', 'iconColor': 'text-blue-600'},
            {'label': 'বুক করা ফ্লাইট', 'value': str(flight_qs.count()), 'inc': '০%', 'icon': 'Plane', 'iconBg': 'bg-indigo-100', 'iconColor': 'text-indigo-600'},
            {'label': 'বুক করা ট্যুর', 'value': str(tour_qs.count()), 'inc': '০%', 'icon': 'Map', 'iconBg': 'bg-green-100', 'iconColor': 'text-green-600'},
            {'label': 'অফলাইন ডিলস', 'value': str(deal_qs.count()), 'inc': '০%', 'icon': 'Briefcase', 'iconBg': 'bg-purple-100', 'iconColor': 'text-purple-600'},
            {'label': 'অ্যাক্টিভ কাস্টমার', 'value': str(customer_qs.count()), 'inc': '০%', 'icon': 'Users', 'iconBg': 'bg-sky-100', 'iconColor': 'text-sky-600'},
        ]
        
        # 2. Area Chart Data
        # Group flights by departure_date since that's the only date we have
        flight_dates = flight_qs.values('departure_time__date').annotate(count=Count('id')).order_by('departure_time__date')
        area_data = []
        for f in flight_dates:
            date_str = f['departure_time__date'].strftime('%d %b')
            area_data.append({
                'name': date_str,
                'flights': f['count'],
                'tours': 0, # Cannot track historical tours
                'visas': 0
            })
            
        # 3. Donut Chart (Customer Sources)
        sources = customer_qs.values('source').annotate(count=Count('id'))
        color_map = {
            'WhatsApp': '#25D366',
            'Messenger': '#0084FF',
            'Direct Call': '#F59E0B',
            'Website': '#8B5CF6'
        }
        donut_data = []
        for s in sources:
            src_name = s['source'] if s['source'] else 'Other'
            donut_data.append({
                'name': src_name,
                'value': s['count'],
                'color': color_map.get(src_name, '#9CA3AF')
            })

        # 4. Recent Bookings (Merged from all listings)
        all_recent = []
        for f in flight_qs.order_by('-id')[:3]:
            all_recent.append({'id': f.id, 'sort_key': f.id, 'customer': f.airline, 'service': 'ফ্লাইট', 'icon': 'Plane', 'date': f.departure_time.strftime('%d %b, %Y'), 'status': 'Available', 'statusColor': 'bg-green-100 text-green-700'})
        for t in tour_qs.order_by('-id')[:3]:
            all_recent.append({'id': t.id, 'sort_key': t.id, 'customer': t.destination, 'service': 'ট্যুর', 'icon': 'Map', 'date': '-', 'status': 'Available', 'statusColor': 'bg-blue-100 text-blue-700'})
        for v in visa_qs.order_by('-id')[:3]:
            all_recent.append({'id': v.id, 'sort_key': v.id, 'customer': v.country, 'service': 'ভিসা', 'icon': 'FileText', 'date': v.processing_time, 'status': 'Available', 'statusColor': 'bg-purple-100 text-purple-700'})
        for u in umrah_qs.order_by('-id')[:3]:
            all_recent.append({'id': u.id, 'sort_key': u.id, 'customer': u.package_name, 'service': 'ওমরাহ', 'icon': 'Moon', 'date': '-', 'status': 'Available', 'statusColor': 'bg-yellow-100 text-yellow-700'})

        for d in deal_qs.order_by('-id')[:3]:
            all_recent.append({'id': d.id, 'sort_key': d.id, 'customer': d.customer_name, 'service': d.service_category, 'icon': 'Briefcase', 'date': d.created_at.strftime('%d %b, %Y'), 'status': 'Available', 'statusColor': 'bg-purple-100 text-purple-700'})
        all_recent.sort(key=lambda x: x['sort_key'], reverse=True)
        recent_bookings = all_recent[:5]

        # 5. Top Destinations (From Tours)
        tours = tour_qs.order_by('-id')[:5]
        top_destinations = []
        for t in tours:
            img_url = ''
            if t.image:
                img_url = request.build_absolute_uri(t.image.url)
            top_destinations.append({
                'name': t.destination,
                'country': t.duration,
                'percent': 100,
                'image': img_url
            })

        # 6. Upcoming Flights
        # Now querying from Deal model for upcoming flights based on travel_date
        deals_flights = Deal.objects.filter(
            service_category__in=['Flight Ticket', 'ফ্লাইট টিকিট'],
            travel_date__gte=timezone.now().date()
        ).order_by('travel_date')[:5]
        
        upcoming_flights = []
        for d in deals_flights:
            upcoming_flights.append({
                'flight': d.airline_name if d.airline_name else 'Unknown Airline',
                'route': d.route_destination,
                'date': d.travel_date.strftime('%d %b, %Y'),
                'status': 'অন টাইম',
                'statusColor': 'bg-green-100 text-green-700'
            })

        # 7. Recent Visas
        visas = visa_qs.order_by('-id')[:5]
        recent_visas = []
        for v in visas:
            recent_visas.append({
                'visa': v.country,
                'type': v.visa_type,
                'time': v.processing_time,
                'status': 'Available',
                'statusColor': 'bg-green-100 text-green-700'
            })

        # 8. Bar Chart Data (Customer Growth)
        months = customer_qs.values('joined_date').annotate(count=Count('id'))
        bar_data_dict = {}
        for m in months:
            month_name = m['joined_date'].strftime('%b')
            if month_name in bar_data_dict:
                bar_data_dict[month_name] += m['count']
            else:
                bar_data_dict[month_name] = m['count']
        
        bar_data = [{'name': k, 'value': v} for k, v in bar_data_dict.items()]

        return Response({
            'topStats': top_stats,
            'areaData': area_data,
            'donutData': donut_data,
            'recentBookings': recent_bookings,
            'topDestinations': top_destinations,
            'upcomingFlights': upcoming_flights,
            'recentVisas': recent_visas,
            'barData': bar_data
        })
