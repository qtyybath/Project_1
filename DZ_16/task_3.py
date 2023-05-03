# 1. За допомогою https://open-meteo.com/ дістати прогноз погоди для 5ти ваших улюблених міст на планеті.
# Реалізувати за допомогою модуля requests з використанням  мультипроцесорності.

#  я в окремий файл винесла мультіпроцесность
# Третя частина першого завдання та третє завдання (процеси)

import requests
import time
import multiprocessing
import json

cities = [{"city": "Heidelberg", "latitude": 49.41, "longitude": 8.69},
          {"city": "Kyiv", "latitude": 50.45, "longitude": 30.52},
          {"city": "Berlin", "latitude": 52.52, "longitude": 13.41},
          {"city": "London", "latitude": 51.51, "longitude": -0.13},
          {"city": "Paris", "latitude": 48.85, "longitude": 2.35}]


def weather_today(cities):
    for city in cities:
        url = f'https://api.open-meteo.com/v1/forecast?latitude=' \
              f'{city["latitude"]}&longitude={city["longitude"]}&hourly=temperature_2m&forecast_days=1'
        response = requests.get(url)
        data = response.json()
        temperature = json.dumps(data["hourly"]["temperature_2m"]).replace("[", " ").replace("]", " ")
        print(f'Temperature in {city["city"]} today: {temperature}°C')


def multiproc():    # ця функуія запускає процеси в довільному порядку
    processes = []
    for city in cities:
        p = multiprocessing.Process(target=weather_today, args=([city], ))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    start = time.time()
    multiproc()
    print(f"Program ended in {time.time() - start}")  # загалтьний час на виконання  0.66-0.76 секунди (показує різний результат)
                                                          # Потоки швидше зпрацювали ніж процеси


def multiproc():        # ця функуія запускає процеси по черезі кожні 2 секунди
    processes = []
    for city in cities:
        p = multiprocessing.Process(target=weather_today, args=([city],))
        processes.append(p)
        p.start()
        time.sleep(2)

    for p in processes:
        p.join()

if __name__ == "__main__":
    start = time.time()
    multiproc()
    print(f"Program ended in {time.time() - start}")   # загалтьний час на виконання  10 секунд, як  мало бути
