import requests

def get_coordinates(address):
    """Get coordinates for an address using Google's Geocoding API"""
    API_KEY = 'YOUR_GOOGLE_API_KEY'
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    params = {
        'address': address,
        'key': API_KEY
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return {
            'lat': location['lat'],
            'lng': location['lng']
        }
    return None 