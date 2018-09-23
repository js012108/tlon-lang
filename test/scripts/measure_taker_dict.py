x = 10

from platform import system as system_name
from os import system as system_call
import socket, datetime, gps, sys, time, Adafruit_DHT, requests, json

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
sensor = Adafruit_DHT.DHT11
pin = 23
lat = 0
lon = 0
time = 0

def gps():
    measure_dict={}
    x = 1
    while x == 1:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                print 'Hora:      ' + str(report.time)
                global time
                time = str(report.time)
                measure_dict['time'] = time
            if hasattr(report, 'lat'):
                print 'Latitud:   ' + str(report.lat)
                global lat
                lat = str(report.lat)
                measure_dict['lat'] = lat
            if hasattr(report, 'lon'):
                print 'Longitud:  ' + str(report.lon)
                global lon
                lon = str(report.lon)
                measure_dict['lon'] = lon
            if hasattr(report, 'speed'):
                print 'Velocidad: ' + str(report.speed)
                measure_dict['speed'] = str(report.speed)
            if hasattr(report, 'track'):
                print 'Rumbo:     ' + str(report.track)
                measure_dict['track'] = str(report.track)
            if hasattr(report, 'head'):
                print report.head
                measure_dict['head'] = str(report.head)
            x= 0
    return measure_dict

try:
    # Ciclo principal infinito
    i = 0
    file = open("measures.txt","w")
    while i<x:
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        measure_dict = gps()
        file.write(json.dumps(measure_dict))
        i += 1
    file.close() 


# Se ejecuta en caso de que falle alguna instruccion dentro del try
except Exception,e:
    # Imprime en pantalla el error e
    print str(e)