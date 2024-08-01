class weather:
    def __init__(self, date, day, info):
        self.date = date
        self.day = day
        self.info = info

n = int(input())

forecasts = []

for _ in range(n):
    date, day, info = tuple(input().split())
    forecasts.append(weather(date, day, info))

rain_forecasts = []

for forecast in forecasts:
    if forecast.info == 'Rain':
        rain_forecasts.append(forecast)
    else:
        pass

rain_forecasts.sort(key = lambda x: x.date)

print(f"{rain_forecasts[0].date} {rain_forecasts[0].day} {rain_forecasts[0].info}")