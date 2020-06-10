import csv
from datetime import datetime
from datetime import date
import sys
import traceback
from collections import defaultdict, Counter
import requests
import time

Input = 'locations.dat'
API_KEY = '0f0eee53cb80d2272c12a87e87e8a609'


def read_input(input_file):
    print("enter function")
    with open(input_file, "r") as csv_file:
        count = 0
        data_reader = csv.reader(csv_file)
        for row in data_reader:
            if count == 0:
                count += 1
                continue
            else:
                count += 1
                yield row


def get_five_day_forecast(lat, lon):
    call = 'http://api.openweathermap.org/data/2.5/forecast?lat={0}&lon={1}&APPID={2}'.format(lat, lon, API_KEY)
    r = requests.post(call)
    return r


def process_api_results(res, loc):
    api_results = []
    res_json = res.json()
    res_list = res_json['list']
    for i in res_list:
        dt = i['dt']
        forecast_date = datetime.fromtimestamp(int(dt)).strftime('%Y-%m-%d')
        forecast_time = datetime.fromtimestamp(int(dt)).strftime('%H:%M:%S')
        weather_code = i['weather'][0]['id']
        temp_kelvin = i['main']['temp']
        temp_celsius = "{0:.0f}".format(temp_kelvin - 273.15)

        api_results.append((loc,
                            forecast_date,
                            forecast_time,
                            weather_code,
                            temp_celsius))
    return api_results


def produce_daily_summary(input_file):
    print("enter produce daily summary")
    weather = defaultdict(lambda: defaultdict(list))
    temp = defaultdict(lambda: defaultdict(list))
    int_f = read_input(input_file)
    for row in int_f:
        LocationID, Longitude, Latitude = row

        r = get_five_day_forecast(Latitude, Longitude)
        # time.sleep(1.1)
        results = process_api_results(r, LocationID)
        for r in results:
            weather[r[0]][r[1]].append(r[3])
            temp[r[0]][r[1]].append(int(r[4]))
    return weather, temp


def main():
    try:
        print("Before file read")
        weather, temp = produce_daily_summary(input_file=Input)
        print(weather)
        # int_f = read_input(input_file=Input)
        # for row in int_f:
        #     LocationID, Longitude, Latitude = row
        #     print("location:{0},latitude:{1},longitude:{2}".format(LocationID, Latitude, Latitude))
    except Exception as e:
        print(sys.exc_info()[0])
        print(e)


if __name__ == '__main__':
    main()
