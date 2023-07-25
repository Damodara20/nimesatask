import requests

def get_weather_data(city):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve weather data.")
        return None

def get_temperature(data, date):
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['temp']
    return None

def get_wind_speed(data, date):
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['wind']['speed']
    return None

def get_pressure(data, date):
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['pressure']
    return None

def main():
    city = "London,us"
    weather_data = get_weather_data(city)
    
    if weather_data is None:
        return

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice (0-3): ")

        if option == "1":
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temperature = get_temperature(weather_data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature} Kelvin")
            else:
                print("Invalid date or data not available for the input date.")
        
        elif option == "2":
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Invalid date or data not available for the input date.")
        
        elif option == "3":
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Invalid date or data not available for the input date.")
        
        elif option == "0":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please try again.")

if _name_ == "_main_":
    main()
