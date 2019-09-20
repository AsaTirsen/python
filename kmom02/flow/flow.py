#!/usr/bin/env python3


"""
villkor och loopar
"""

number_of_apples = 13

if number_of_apples > 10:
    print("Du har mer än 10 äpplen")

# skriver ut: Du har mer än 10 äpplen

number_of_apples = 13

if number_of_apples > 10:
    print("Du har mer än 10 äpplen")

print("Nu är vi klara med if-satsen")
# skriver ut:
# Du har mer än 10 äpplen
# Nu är vi klara med if-satsen

number_of_apples = 9

if number_of_apples > 10:
    print("Du har mer än 10 äpplen")
elif number_of_apples <= 10 and number_of_apples > 5:
    print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
else:
    print("Du har nog varit hungrig och ätit upp dina äpplen")

print("Nu är vi klara med if-satsen")

# skriver ut:
# Du blev snabbt mätt och åt bara upp några av dina äpplen
# Nu är vi klara med if-satsen

type_of_fruit = "päron"
number_of_fruits = 13

if number_of_fruits > 10:
    if type_of_fruit == "äpple":
        print("Du har mer än 10 äpplen")
    else:
        print("Du har mer än 10 frukter")

    print("Nu är vi klara med den inre if-satsen")

print("Nu är vi klara med den yttre if-satsen")

# skriver ut:
# Du har mer än 10 frukter
# Nu är vi klara med den inre if-satsen
# Nu är vi klara med den yttre if-satsen

# for loop
for i in range(10):
    print(i)

print("Jag är klar med loopen")

# skriver ut:
# siffrorna 0-9 i följd, notera inte 10
# Jag är klar med loopen

for _ in range(5):
    print("Python är ett spännande programmeringsspråk")

# skriver ut:
# Python är ett spännande programmeringsspråk 5 gånger

for letter in "räksmörgås":
    if letter in "åäö":
        print(letter)

#skriver ut:
# ä
# ö
# å
#notera behöver inte skriva range()

number = 2

while number < 20:
    print(number)
    number = number + number

# skriver ut: 2 4 8 16


while True:
    user_input = input("Skriv in antal äpplen (eller q för avslut): ")
    if user_input == "q":
        print("Du är nu klar med att äta äpplen.")
        print("Hej då!")
        break
        #notera break för att avsluta frågan till användaren
    else:
        try:
            number_of_apples = int(user_input)
        except ValueError:
            print("Oj! Du skrev inte in en siffra.")
            continue
            #try except plockar upp ev fel, continue gör att loopen börjar om
        if number_of_apples > 10:
            print("Du har mer än 10 äpplen")
        elif number_of_apples <= 10 and number_of_apples > 5:
            print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
        else:
            print("Du har nog varit hungrig och ätit upp dina äpplen")




num_one = 0
num_two = 0
num_three = 1
counter = 0
while num_one + num_two + num_three < 28:
    num_one += 1
    if num_one + num_two == num_three:
        counter += 1
    num_two += 1
    if num_one + num_two == num_three:
        counter += 1
    num_three += 1
    if num_one + num_two == num_three:
        counter += 1

var1 = 0
var2 = 0
var3 = 1
while var1 < 10:
    if var1 + var2 == var3:
        print("match")
    var1 += 1
    print(var1, "var1")
    while var2 < 10:
        if var1 + var2 == var3:
            print("match")
        var2 += 1
        print(var2, "var2")
        while var3 < 10:
            if var1 + var2 == var3:
                print("match")
            var3 += 1
            print(var3, "var3")
