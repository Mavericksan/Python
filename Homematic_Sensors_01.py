import matplotlib.pyplot as plt
import datetime as dt


with open('homematic_467-humidity.csv', 'r') as f:
    i = 0
    for Zeile in f:
        if i >= 1:
            #Ignore first line of file
            DatumTimeStr, SensorValueStr = Zeile.split(';')
            #print(DatumTimeStr,'   --> ', SensorValueStr)
            datum = (dt.datetime.strptime(DatumTimeStr, '%d.%m.%Y %H:%M')).date()
            #print(datum)
        i =+ 1    
        
        