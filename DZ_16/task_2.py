# 1. За допомогою https://open-meteo.com/ дістати прогноз погоди для 5ти ваших улюблених міст на планеті.
# Реалізувати за допомогою модуля requests з використанням мультипотоковості і мультипроцесорності.
# 3. Вивести різницю по часу виконання програми використовуючи потоки і процеси.

# Друга частина першого завдання та третє завдання (потоки)


import threading
import requests
import time
import json

cities = [{"city": "Heidelberg", "latitude": 49.41, "longitude": 8.69},
          {"city": "Kyiv", "latitude": 50.45, "longitude": 30.52},
          {"city": "Berlin", "latitude": 52.52, "longitude": 13.41},
          {"city": "London", "latitude": 51.51, "longitude": -0.13},
          {"city": "Paris", "latitude": 48.85, "longitude": 2.35}]


def multi_thread():
    result = []

    def weather_today(cities):
        for city in cities:
            url = f'https://api.open-meteo.com/v1/forecast?latitude=' \
                  f'{city["latitude"]}&longitude={city["longitude"]}&hourly=temperature_2m&forecast_days=1'
            response = requests.get(url)
            data = response.json()
            temperature = json.dumps(data["hourly"]["temperature_2m"]).replace("[", " ").replace("]", " ")
            print(f'Temperature in {city["city"]} today: {temperature}°C')

    start = time.time()
    threads = []
    for city in cities:
        t = threading.Thread(target=weather_today, args=([city],))
        # потоки запускаються в довільній формі
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for item in result:
        print(item)

    end = time.time()
    print(f"Multi thread time is {end - start}")  # загалтьний час на виконання  0.12 секунди.

if __name__ == "__main__":
    multi_thread()
