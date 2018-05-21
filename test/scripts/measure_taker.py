x = 10

from platform import system as system_name
from os import system as system_call
import socket, datetime, gps, sys, time, Adafruit_DHT, requests

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
sensor = Adafruit_DHT.DHT11
pin = 23
lat = 0
lon = 0
time = 0

def gps():
    x = 1
    while x == 1:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                print 'Hora:      ' + str(report.time)
                global time
                time = str(report.time)
            if hasattr(report, 'lat'):
                print 'Latitud:   ' + str(report.lat)
                global lat
                lat = str(report.lat)
            if hasattr(report, 'lon'):
                print 'Longitud:  ' + str(report.lon)
                global lon
                lon = str(report.lon)
            if hasattr(report, 'speed'):
                print 'Velocidad: ' + str(report.speed)
            if hasattr(report, 'track'):
                print 'Rumbo:     ' + str(report.track)
            if hasattr(report, 'head'):
                print report.head
            x= 0

try:
    # Ciclo principal infinito
    i = 0
    while i<x:
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        gps()
        r = requests.post("http://13.58.53.154/map", data={'temp': temperatura, 'hum': humedad, 'longitud' : lon, 'latitud' : lat, 'humsuelo' : 0, 'precipitacion' : 6, 'datemed' : time})
        print(temperatura, humedad, lon, lat)
        i += 1


# Se ejecuta en caso de que falle alguna instruccion dentro del try
except Exception,e:
    # Imprime en pantalla el error e
    print str(e)