#!/usr/bin/env python3
#Programmet konverterar höjd över havet, hastighet och temperatur från metric till imperial
"""
Programmet konverterar höjd över havet, hastighet och temperatur från metric till imperial
"""
altitude_m = input("Skriv höjd över havet i meter: ")
velocity_m = input("Skriv hastighet i km/h: ")
temp_c = input("Skriv in temperatur utanför planet i Celsius: ")

feet = round(float(altitude_m) * 3.28084, 2)
mph = round(float(velocity_m) * 0.62137, 2)
temp = int(temp_c) * 9/5 + 32

print("Höjd över havet (feet) " + str(feet))
print("Hastighet (mph) " + str(mph))
print("Temperatur utanför flygplanet (Fahrenheit) " + str(temp))
