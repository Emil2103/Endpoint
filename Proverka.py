import requests
import json

def get_weather_data(api_url, latitude, longitude, start_date, end_date, prob=0.5):
    payload = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "prob": prob
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    api_url = "http://localhost:8000/weather-data"  # URL FastAPI сервиса
    latitude = 52.52
    longitude = 13.41
    start_date = "2024-05-02"
    end_date = "2024-05-16"
    prob = 0.5
    
    try:
        weather_data = get_weather_data(api_url, latitude, longitude, start_date, end_date, prob)
        print(weather_data)
    except Exception as e:
        print(f"An error occurred: {e}")
