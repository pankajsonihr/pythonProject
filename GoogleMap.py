import requests
import API


def search_location_in_city(location):
    # Your Google Maps Places API key
    api_key = API.map_key

    # Set up the URL for the Places API search
    url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
    params = {
        'key': api_key,
        'input': location,
        'inputtype': 'textquery',
        'fields': 'geometry,name',
        'locationbias': f'circle:5000@{"Sudbury"}',
    }

    # Send the API request
    response = requests.get(url, params=params)

    # Parse the response
    data = response.json()
    if data['status'] != 'OK':
        print(f"Error: {data['status']}")
        return None

    # Extract the coordinates and name of the first result
    result = data['candidates'][0]
    name = result['name']
    lat = result['geometry']['location']['lat']
    lng = result['geometry']['location']['lng']

    # Generate the URL for the location on Google Maps
    maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"

    # Return the URL
    return maps_url

