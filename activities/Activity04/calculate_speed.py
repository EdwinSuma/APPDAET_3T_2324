distance_km = 150
time_hours = 2

distance_miles = distance_km / 1.6
distance_meters = distance_km * 1000

time_seconds = time_hours * 3600

speed_kmph = distance_km / time_hours
speed_mph = distance_miles / time_hours
speed_mps = distance_meters / time_seconds

print(f"Speed in kilometers per hour: {speed_kmph} km/h")
print(f"Speed in miles per hour: {speed_mph} mph")
print(f"Speed in meters per second: {speed_mps} m/s")
