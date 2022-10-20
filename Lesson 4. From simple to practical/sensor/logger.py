from datetime import datetime as dt
from time import time

def temperatur_logger(data):
    time=dt.now().strftime('%H:%M')
    with open('log.scv', 'a') as file:
        file.write('{};temperature;{}\n'
                    .format(time,data))

def preassure_logger(data):
    time=dt.now().strftime('%H:%M')
    with open('log.scv', 'a') as file:
        file.write('{};preassure;{}\n'
                    .format(time,data))

def wind_speed_logger(data):
    time=dt.now().strftime('%H:%M')
    with open('log.scv', 'a') as file:
        file.write('{};wind_speed;{}\n'
                    .format(time,data))