# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:35:10 2020

@author: amanb
"""

import serial
import time
import schedule
import urllib
from urllib.request import urlopen

def update_data(i, n):
    data=urlopen('https://api.thingspeak.com/update?api_key=04HQ0A9PSJROEVZU&field'+str(i)+'='+str(n))
    print(data)
    
def main_func():
    arduino = serial.Serial('com1', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')

    for item in list_values:
        list_in_floats.append(float(item))
    a=list_in_floats[0];
    #b=list_in_floats[1];
    #c=list_in_floats[2];
    update_data(1,a);
    #update_data(2,b);
    #update_data(3,c);
    print(f'Collected readings from Arduino: {list_in_floats}')
      
    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
   
    
def main_func_2():
    arduino = serial.Serial('com1', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')

    for item in list_values:
        list_in_floats.append(float(item))
    #a=list_in_floats[0];
    b=list_in_floats[1];
    #c=list_in_floats[2];
    #update_data(1,a);
    update_data(2,b);
    #update_data(3,c);
    print(f'Collected readings from Arduino: {list_in_floats}')
      
    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()

def main_func_3():
    arduino = serial.Serial('com1', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')

    for item in list_values:
        list_in_floats.append(float(item))
    #a=list_in_floats[0];
    #b=list_in_floats[1];
    c=list_in_floats[2];
    #update_data(1,a);
    #update_data(2,b);
    update_data(3,c);
    print(f'Collected readings from Arduino: {list_in_floats}')
      
    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
  
    
# ----------------------------------------Main Code------------------------------------
# Declare variables to be used
list_values = []
list_in_floats = []
list_values_1= []
list_in_floats_1 = []


print('Program started')

# Setting up the Arduino
schedule.every(2).seconds.do(main_func)
schedule.every(5).seconds.do(main_func_1)

while True:
    schedule.run_pending()
    time.sleep(1)
