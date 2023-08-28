import requests

# Replace with your actual coordinates
start_coords = "90.399452,23.777176"  # Dhaka
end_coords = "91.83168,22.3384"    # Chittagong

url = f"http://router.project-osrm.org/route/v1/car/{start_coords};{end_coords}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    distance = data['routes'][0]['distance'] / 1000  # Convert to kilometers
    duration = data['routes'][0]['duration'] / 3600  # Convert to hours
    print(f"Distance: {distance:.2f} km")
    print(f"Duration: {duration:.2f} hours")
else:
    print("Error calculating route:", response.text)
