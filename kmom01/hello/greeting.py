#!/usr/bin/env python3
#Programmet skriver ut en hälsning
"""
Programmet skriver ut en hälsning
"""
year = 2019
name = input("Skriv ditt namn: ")
age = input("Skriv in din ålder: ")
year_born = year - int(age)
greeting = "Hej " + name + ", du är " + age + " år gammal och föddes år " + str(year_born)
print(greeting)
