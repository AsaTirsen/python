#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!`   `4!!!!!!!!!!~4!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   <~:   ~!!!~   ..  4!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  ~~~~~~~  '  ud$$$$$  !!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  ~~~~~~~~~: ?$$$$$$$$$  !!!!!!!!!!!!!!
!!!!!!!!!!!`     ``~!!!!!!!!!!!!!!  ~~~~~          "*$$$$$k `!!!!!!!!!!!!!
!!!!!!!!!!  $$$$$bu.  '~!~`     .  '~~~~      :~~~~          `4!!!!!!!!!!!
!!!!!!!!!  $$$$$$$$$$$c  .zW$$$$$E ~~~~      ~~~~~~~~  ~~~~~:  '!!!!!!!!!!
!!!!!!!!! d$$$$$$$$$$$$$$$$$$$$$$E ~~~~~    '~~~~~~~~    ~~~~~  !!!!!!!!!!
!!!!!!!!> 9$$$$$$$$$$$$$$$$$$$$$$$ '~~~~~~~ '~~~~~~~~     ~~~~  !!!!!!!!!!
!!!!!!!!> $$$$$$$$$$$$$$$$$$$$$$$$b   ~~~    '~~~~~~~     '~~~ '!!!!!!!!!!
!!!!!!!!> $$$$$$$$$$$$$$$$$$$$$$$$$$$cuuue$$N.   ~        ~~~  !!!!!!!!!!!
!!!!!!!!! **$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Ne  ~~~~~~~~  `!!!!!!!!!!!
!!!!!!!!!  J$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$N  ~~~~~  zL '!!!!!!!!!!
!!!!!!!!  d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$c     z$$$c `!!!!!!!!!
!!!!!!!> <$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$> 4!!!!!!!!
!!!!!!!  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  !!!!!!!!
!!!!!!! <$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*"   ....:!!
!!!!!!~ 9$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$e@$N '!!!!!!!
!!!!!!  9$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  !!!!!!!
!!!!!!  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""$$$$$$$$$$$~ ~~4!!!!
!!!!!!  9$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$Lue  :::!!!!
!!!!!!> 9$$$$$$$$$$$$" '$$$$$$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$  !!!!!!!
!!!!!!! '$$*$$$$$$$$E   '$$$$$$$$$$$$$$$$$$$$$$$$$$$u.@$$$$$$$$$E '!!!!!!!
!!!!~`   .eeW$$$$$$$$   :$$$$$$$$$$$$$***$$$$$$$$$$$$$$$$$$$$u.    `~!!!!!
!!> .:!h '$$$$$$$$$$$$ed$$$$$$$$$$$$Fz$$b $$$$$$$$$$$$$$$$$$$$$F '!h.  !!!
!!!!!!!!L '$**$$$$$$$$$$$$$$$$$$$$$$ *$$$ $$$$$$$$$$$$$$$$$$$$F  !!!!!!!!!
!!!!!!!!!   d$$$$$$$$$$$$$$$$$$$$$$$$buud$$$$$$$$$$$$$$$$$$$$"  !!!!!!!!!!
!!!!!!! .<!  #$$*"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*  :!!!!!!!!!!!
!!!!!!!!!!!!:   d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#  :!!!!!!!!!!!!!
!!!!!!!!!!!~  :  '#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*"    !!!!!!!!!!!!!!!
!!!!!!!!!!  !!!!!:   ^"**$$$$$$$$$$$$$$$$$$$$**#"     .:<!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!:...                      .::!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Kitty. I know it all. What can I do you for?")
    print("1) Present yourself to Kitty.")
    print("2) Give me a temperature in C, and I'll convert it to F.")
    print("3) Give me a word and a number and I'll write the word number times.")
    print("4) Give me a series of numbers and I'll calculate sum and average.")
    print("5) Give me atleast two numbers and I'll tell you which is bigger.")
    print("6) Give me a string and I'll do some magic to it.")
    print("7) Give me a word and I'll check if the word is an isogram.")
    print("A1) Give me two strings and I'll compare them")
    print("A2) Give me a number and let me know how many times I should multiply to get all numbers 0-9")
    print("A3) Give me a string with 1 or more tabs and I'll replace them with 3 spaces.")
    print("A4) Give me two names and I'll make a spiffy new combo")
    print("A5) Give me a series of results; use lowercase for positive numbers and uppercase for negative numbers")
    print("q) Quit.")

    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - and welcome back anytime!")
        break

    elif choice == "1":
        name = input("What is your name? ")
        print("\nKitty says:\n")
        print("Hello %s - your awesomeness!" % name)
        print("What can I do you for?!")

    elif choice == "2":
        temp_c = input("Give me a temperature i C: ")
        temp_f = round(float(temp_c) * 9 / 5 + 32, 1)
        print(temp_c, " in Farhrenheit is ", temp_f, )

    elif choice == "3":
        word = input("Give me a word: ")
        number = input("Give me an integer: ")
        print((word + " ") * int(number))

    elif choice == "4":
        num_sum = 0
        counter = 0
        average = 0
        while True:
            user_input = input("Give me numbers. When done, write 'done': ")
            if user_input == "done":
                break
            else:
                num = float(user_input)
                num_sum += float(num)
                counter += 1.0
                average = round(num_sum / counter, 2)
        print("Your sum is: ", num_sum, " and your average is: ", average)

    elif choice == "5":
        smallest = None
        while True:
            user_input = input("Give me atleast two numbers. When done, write 'done': ")
            if user_input == "done":
                print("Okie, you wanna stop now!")
                break
            else:
                num = float(user_input)
                if smallest is None:
                    smallest = num
                elif num > smallest:
                    smallest = num
                    print(num, " is bigger than the previous one")
                elif num == smallest:
                    smallest = num
                    print(num, " is equal to the previous one")
                else:
                    smallest = num
                    print(num, " is smaller than the previous one")

    elif choice == "6":
        while True:
            user_input = input("Give me a string and I'll do some magic to it: ")
            str_coll = ""
            counter = 1
            for letter in user_input:
                str_coll += letter * counter
                if counter < len(user_input):
                    str_coll = str_coll + "-"
                    counter += 1
                else:
                    print(str_coll)

    elif choice == "7":
        user_input = []
        count = 0
        letter = ""
        while True:
            user_input = input("Give me a word and I'll check if the word is an isogram: ")
            # if user_input == "done":
            #     print("Okie, you wanna stop now!")
            #     break
            for letter in user_input:
                count = user_input.count(letter)
            if count > 1:
                print(user_input + " is not an isogram")
            else:
                print(user_input + " is an isogram")

    elif choice == "A1":
        new_two = ""
        while True:
            user_input_one = input("Give me a string: ")
            user_input_two = input("Give me a second string: ")
            for letter in user_input_two:
                if letter in user_input_one:
                    new_two += letter
                else:
                    break
            if not new_two:
                print("no match")
            else:
                print("match")
            break


    elif choice == "A2":
        counter = 0
        input_str = ""
        new_string = ""
        input_one = input("Give me a number: ")
        input_two = input("How many times do we need to multiply?: ")
        while True:
            number_seq = "0123456789"
            for i in input_one:
                if i in number_seq:
                    number_seq = number_seq.replace(i, "")
            if number_seq == "":
                break
            input_one = int(input_one) * 2
            input_one = str(input_one)
            counter += 1
        if counter > int(input_two):
            print(-1)
        else:
            print(counter, input_one)



    elif choice == "A3":
        while True:
            counter = 0
            string = ""
            user_input = input("Give me a string with at least 1 tab: ")
            for letter in user_input:
                if letter == '\t':
                    string = user_input.replace('\t', '   ')
                else:
                    "Write a string with at least 1 tab."
            print(string)


    elif choice == "A4":
        while True:
            user_input_one = input("Give me a first name: ")
            user_input_two = input("Give me another first name: ")
            vowels = "a e i o u y"
            new_name = ""
            new_name_two = ""
            for letter in user_input_one:
                if letter in vowels:
                    index = user_input_one.index(letter)
                    new_name = user_input_one[:index]
                    break
            for letter in user_input_two:
                if letter in vowels:
                    index = user_input_two.index(letter)
                    new_name_two = user_input_two[index:]
                    break
            print(new_name + new_name_two)

    elif choice == "A5":
        while True:
            user_input = input(
                "Give me a series of results; use lowercase for positive numbers and uppercase for negative numbers: ")
            final_string = ""
            letters = ""
            for i in range(0, len(user_input), 2):
                letter = user_input[i].upper()
                if letter not in letters:
                    letters += letter

            for letter in letters:
                total = 0
                for i in range(0, len(user_input), 2):
                    number = int(user_input[i + 1])
                    if user_input[i] == letter.lower():
                        total -= number
                    elif user_input[i] == letter.upper():
                        total += number
                    else:
                        continue
                final_string += (letter.lower() + str(total) + ", ")
                print(final_string)



    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
