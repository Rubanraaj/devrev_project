from django.core.management.base import BaseCommand
from flight.models import Flight
import pandas as pd
from datetime import timedelta

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv("flight_details.csv")
        df['depart_time'] = pd.to_datetime(df['depart_time'])
        df['arrival_time'] = pd.to_datetime(df['arrival_time'])
        
        for _, row in df.iterrows():
            duration_parts = row['duration'].split(':')
            duration = timedelta(hours=int(duration_parts[0]), minutes=int(duration_parts[1]))
            
            flight = Flight(
                origin=row['origin'],
                destination=row['destination'],
                depart_time=row['depart_time'].strftime('%Y-%m-%d %H:%M:%S'),  # Format to include time
                duration=duration,
                arrival_time=row['arrival_time'].strftime('%Y-%m-%d %H:%M:%S'),  # Format to include time
                plane=row['plane'],
                airline=row['airline'],
                fare=row['fare'],
                total_seats=row['total_seats']
            )
            flight.save()
