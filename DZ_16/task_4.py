# 2. Знайти середню температуру по прогнозу для кожного міста і вивести в якому місті зараз найспекотніше.
# Перша частина третього завдання (потоки)

cities = [{"city": "Heidelberg", "latitude": 49.41, "longitude": 8.69},
          {"city": "Kyiv", "latitude": 50.45, "longitude": 30.52},
          {"city": "Berlin", "latitude": 52.52, "longitude": 13.41},
          {"city": "London", "latitude": 51.51, "longitude": -0.13},
          {"city": "Paris", "latitude": 48.85, "longitude": 2.35}]

import requests
import json
import threading
import queue

results = []

def weather_today(cities):
    for city in cities:
        url = f'https://api.open-meteo.com/v1/forecast?latitude=' \
              f'{city["latitude"]}&longitude={city["longitude"]}&hourly=temperature_2m&forecast_days=1'
        response = requests.get(url)
        data = response.json()
        temperature = data["hourly"]["temperature_2m"]
        average_temperature = json.dumps([round((sum(temperature) / len(temperature)), 1)]).replace("[", " ").replace("]", " ")
        print(f'Average temperature in {city["city"]} today: {average_temperature}°C')
        t = [city["city"], average_temperature]
        results.append(t)
    return results


def max_temperature(cities, queue):
    trt = weather_today(cities)
    y = max([i[1] for i in [j for j in trt]])
    hottest_city = ([k for k, v in trt if v == y][0])
    queue.put(f"Maximum temperature in the city: {hottest_city} ")


def start_threads(num_threads):
    q = queue.Queue()
    threads = []

    for i in range(num_threads):
        t = threading.Thread(target=max_temperature, args=(cities, q))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    results = []
    while not q.empty():
        results.append(q.get())
        cleaned_result = results[0].replace('[', '').replace(']', '').replace("'", '').strip()
        return cleaned_result


print(start_threads(1))
