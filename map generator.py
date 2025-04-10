import requests
import folium
import time
import webbrowser

def get_location(ip=""):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    
    if data["status"] == "fail":
        print("Unable to fetch location. Please try again.")
        return None
    
    return data

def display_map(lat, lon, location):
    print("Generating your location map... Please wait.")
    time.sleep(1.5)
    
    # Create an interactive map
    map = folium.Map(location=[lat, lon], zoom_start=10)

    # Custom marker
    folium.Marker(
        [lat, lon],
        popup=f"<b>{location}</b>",
        tooltip="Click to see details",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(map)

    # Save and open map
    map.save("geolocation_map.html")
    webbrowser.open("geolocation_map.html")

def main():
    print("Welcome to the Geolocation Tracker!")
    time.sleep(1)
    print("Fetching your location...")

    # Get location for the user's own IP
    data = get_location()
    
    if not data:
        return

    # Extract details
    lat, lon = data['lat'], data['lon']
    location = f"{data['city']}, {data['regionName']}, {data['country']}"
    isp = data['isp']
    timezone = data['timezone']
    
    print("\nLocation Details:")
    print(f"City: {data['city']}")
    print(f"Region: {data['regionName']}")
    print(f"Country: {data['country']} ({data['countryCode']})")
    print(f"Timezone: {timezone}")
    print(f"ISP: {isp}")
    print(f"Latitude: {lat}, Longitude: {lon}")

    # Display on map
    display_map(lat, lon, location)

    # Ask if user wants to track another IP
    while True:
        another = input("\nDo you want to track another IP? (yes/no): ").strip().lower()
        if another == "yes":
            ip = input("Enter an IP address: ").strip()
            data = get_location(ip)
            if data:
                lat, lon = data['lat'], data['lon']
                location = f"{data['city']}, {data['regionName']}, {data['country']}"
                display_map(lat, lon, location)
        elif another == "no":
            print("Exiting... Stay safe online!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()