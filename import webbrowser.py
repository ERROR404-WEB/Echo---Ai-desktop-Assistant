import webbrowser
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

def googlemaps(place):
    geolocator = Nominatim(user_agent='your-app-name/1.0')

    try:
        location = geolocator.geocode(place, addressdetails=True)
        
        if location:
            target_loc = location.latitude, location.longitude
            location_data = location.raw['address']
            target = {'city': location_data.get('city', ''),
                      'state': location_data.get('state', ''),
                      'country': location_data.get('country', '')}
            current_loc = geolocator.geocode('me', addressdetails=True)
            current_latlon = current_loc.latitude, current_loc.longitude
            distance = great_circle(current_latlon, target_loc).kilometers
            distance = round(float(distance), 2)
            url_place = f"https://www.google.com/maps/place/{location.latitude},{location.longitude}"
            webbrowser.open(url_place)
            speak(target)
            speak(f"{place} is {distance} kilometers away from your location.")
        else:
            print(f"Location not found for: {place}")

    except Exception as e:
        print(f"Error: {e}")

googlemaps("india")