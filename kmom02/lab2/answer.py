#!/usr/bin/env python3

"""
9a894b788bccc4b71262306ac96cb48a
python
lab2
v3
asti18
2019-09-03 03:16:49
v4.0.0 (2019-03-05)

Generated 2019-09-03 05:16:50 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - python
#
# In this exercise we will look into flow-control. If-statements, for-loops
# and while-loops.
#



# --------------------------------------------------------------------------
# Section 1. Boolean operators and if-statements
#
# The basics of boolean operators and if-statements.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create three variables representing dice values: `dice1` = 5, `dice2` = 1
# and `dice3` = 3.
#
# Answer with the boolean value of the expression '`dice1` is greater than
# `dice2`'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice1 = 5
dice2 = 1
dice3 = 3

boolean1 = dice1 > dice2


ANSWER = boolean1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Sum the three variables `dice1`, `dice2` and `dice3`.
#
# Use an if-statement to decide if the sum of the three variables i greater
# than 11. If the sum is greater than 11 answer with 'big' otherwise answer
# with 'small'.
#
# Write your code below and put the answer into the variable ANSWER.
#
sum_dice = dice1 + dice2 + dice3
if sum_dice > 11:
    result = "big"
else:
    result = "small"



ANSWER = result
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Add the sum of `dice4` = 1 and `dice5` = 5 to the sum of the three other
# dices.
#
# Use an if, elseif, else statement to check the total value of the dices.
# Answer with 'small' if the sum is smaller than 11, 'intermediate' if the
# sum is greater than or equal to 11 but smaller than 21. If the sum is
# greater than or equal to 21 answer with 'big'.
#
# Write your code below and put the answer into the variable ANSWER.
#
dice4 = 1
dice5 = 5
sum_more_dices = sum_dice + dice4 + dice5
if sum_more_dices < 11:
    result = "small"
elif sum_more_dices >= 11 and sum_more_dices < 21:
    result = "intermediate"
else:
    result = "big"


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a variable `summer_word` containing the word 'vacation'.
#
# Answer with True if `summer_word` contains the letter 's' otherwise answer
# with False.
#
# Tip: Use the `in` operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

summer_word = "vacation"
letter = "s"
result_range = letter in summer_word

ANSWER = result_range

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. For-loops
#
# The basics of iteration and for-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Loop through the numbers 0 to 10 (10 included) and concatenate a string
# with the numbers comma-separated. You should have a comma at the end of the
# string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#
i = 0
r_var = ""
for i in range(0, 11):
    r_var = r_var + str(i) + ','
ANSWER = r_var


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Loop through the letters of the variable `summer_word` from above.
# Concatenate the consonants from `summer_word` and answer with the new word.
#
# Tip: Create a string that contains consonants and check if each letter is
# in it.
#
# Write your code below and put the answer into the variable ANSWER.
#
result_cons = ""
result_word = ""
letter = ""
consonants = "bcdfghjklmnpqrstvxz"
for letter in summer_word:
    if letter in consonants:
        result_cons += letter

ANSWER = result_cons

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Loop through all numbers from 10 to 68 both numbers included. Add all odd
# (udda) numbers together and answer with the result.
#
# Tip: Use the modulus % operator.
#
# Write your code below and put the answer into the variable ANSWER.
#
num_range = 0
num = 0
for num in range(10, 69):
    if num % 2 != 0:
        num_range = num_range + num

ANSWER = num_range

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. While-loops
#
# The basics of while-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (1 points)
#
# Create a while-loop that starts at value 3 and ends when the value is
# greater than 21, the value should be incremented by 3 for each iteration.
# Concatenate a string with the values comma-separated. You should have a
# comma at the end of the string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_val = 3
val_coll = ""
while num_val < 22:
    val_coll = val_coll + str(num_val) + ","
    num_val += 3

ANSWER = val_coll

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (1 points)
#
# Create a while-loop that subtracts 9 from 16, 49 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#

counter = 1
subtract = 16
while counter < 50:
    subtract -= 9
    counter += 1

ANSWER = subtract

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.3 (1 points)
#
# Create a while-loop that calculates the factorial number for 9, 9!. The
# factorial of a number is the number multiplied by all smaller integers > 1.
# The factorial of 9 is `9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1`. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.

num_fact = 9
count_fact = 9
while count_fact > 1:
    num_fact = num_fact * (count_fact -1)
    count_fact -= 1

ANSWER = num_fact

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.3", ANSWER, True)

# --------------------------------------------------------------------------
# Section 4. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.1 (3 points)
#
# Use a for-loop or a while-loop to reverse the word 'disproportionality'.
#
# Answer with the reversed word.
#
# Write your code below and put the answer into the variable ANSWER.
#
word = "disproportionality"
letter = ""

for w in word:
    letter = w + letter

ANSWER = letter

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.2 (3 points)
#
# Swedish numberplates consist of three letters and three numbers. The
# numbers range from 001 to 999. Using one of the four common rules of
# arithmetics (+, -, *, /), on how many of the numberplates can the two first
# numbers give the third number?
#
# Examples:
# 'ABC123' can be combined to 1 + 2 = 3. So this numberplate is good.
# 'ABC129' 1 and 2 cannot be combined to give 9 using the four rules of
# arithmetics, so this does not work.
#
# Order matters, so only use 1 +-*/ 2 = 3 and not 2 +-/* 1 = 3.
#
# Do not count multiple times if more than one rule of arithmetics work.
#
# Answer with the number of numberplates.
#
# Write your code below and put the answer into the variable ANSWER.
#

# range_one = range(0, 10)
# range_two = range(0, 10)
# range_three = range(1, 10)
# for i in range_one:
#     print("i", i)
#     for j in range_two:
#         print("j", j)
#         for k in range_three:
#             print("k", type(k))
#             try:
#                 if range_two[j] + range_one[i] == range_three[k]:
#                     counter += 1
#                     print("addition")
#                 elif range_two[j] - range_one[i] == range_three[k]:
#                     counter += 1
#                     print("subtraction")
#                 elif range_one[i] - range_two[j] == range_three[k]:
#                     counter += 1
#                     print("subtraction")
#                 elif range_two[j] * range_one[i] == range_three[k]:
#                     counter += 1
#                     print("mp")
#                 elif range_two[j] / range_one[i] == range_three[k]:
#                     counter += 1
#                     print("div")
#                 elif range_one[i] / range_two[j] == range_three[k]:
#                     counter += 1
#                     print("div")
#             except ZeroDivisionError:
#                 print("divby0")





# num_one= 0
# num_two = 0
# num_three = 1
# counter= 0
# list_of_lists = 0
# num_list = [0, 0, 1]
# for i in num_list:
#     if i < 9:
#         i = i + 1
#         print(i)
#         num_list += [i]
#         list_of_lists = num_list
#         print(num_list)
# for i in range(0, len(list_of_lists), 3):
#     print(list_of_lists[i:i + 3])
# for i in list_of_lists:
#     try:
#         if list_of_lists[0] + list_of_lists[1] == list_of_lists[2]:
#             print("match")
#             counter += 1
#         elif num_list[0] - num_list[1] == num_list[2]:
#             print("match")
#             counter += 1
#         elif num_list[0] * num_list[1] == num_list[2]:
#             print("match")
#             counter += 1
#         elif num_list[0] / num_list[1] == num_list[2]:
#             print("match")
#             counter += 1
#     except ZeroDivisionError:
#          print("divby0")



# while num_one + num_two + num_three < 28:
#     while num_one < 9:

#         num_one += 1
#         print(num_one, "var1")
#     while num_two < 9:
#         try:
#             if num_one + num_two == num_three:
#                 print("match")
#                 counter += 1
#             elif num_one - num_two == num_three:
#                 print("match")
#                 counter += 1
#             elif num_one * num_two == num_three:
#                 print("match")
#                 counter += 1
#             elif num_one / num_two == num_three:
#                 print("match")
#                 counter += 1
#         except ZeroDivisionError:
#             print("divby0")
#         num_two += 1
#         print(num_two, "var2")
#     while num_three < 9:
#         try:
#             if num_one + num_two == num_three:
#                 print("match")
#                 counter += 1
#             elif num_one - num_two == num_three:
#                 print("match")
#                 counter += 1
#             elif num_one * num_two == num_three:
#                 print("match")
#                 counter += 1
#             elif num_one / num_two == num_three:
#                 print("match")
#                 counter += 1
#         except ZeroDivisionError:
#             print("divby0")
#         num_three += 1
#         print(num_three, "var3")
# print(counter)
#


# list1 = [123]
# list2 = [456]
# list3 = [789]
# for i in list1:
#     print(list1)
#     for j in list2:
#         print(list2)
#         for k in list3:
#             print(list3)
#


# list = [0, 0, 1]
# counter = 0
# while list[0] < 10:
#     list[0] += 1
#     if list[0] + list[1] == list[2]:
#         counter += 1
#     while list[1] < 10:
#         list[1] += 1
#         if list[0] + list[1] == list[2]:
#             counter += 1
#         while list[2] < 10:
#             if list[0] + list[1] == list[2

    # elif list[0] - list[1] == list[2]:
    #     counter += 1
    # elif list[0] * list[1] == list[2]:
    #     counter += 1
    # elif list[0] / (list[1] + 1) == list[2]:
    #     counter += 1



# list1 = [0]
# list2 = [0]
# list3 = [1]
#
# for i in list1:
#     list1 = [i + 1]
#     if list1[i] + list2[j]:
#
#     for j in list2:
#         list2 = j + 1
#         for k in list3:
#             list3 = k + 1



# ental = 0
# tiotal = 0
# hundratal = 1
# counter_total = 0
#
#
# while hundratal < 10:
#     ental = ental + 1
#     if ental + tiotal == hundratal:
#         counter_total += 1
#         #ental += 1
#         hundratal += 1
#         continue
#     elif ental - tiotal == hundratal:
#         counter_total += 1
#         ental += 1
#         hundratal += 1
#         continue
#     elif ental * tiotal == hundratal:
#         counter_total += 1
#         ental += 1
#         hundratal += 1
#         continue
#     elif (ental+0.1) / (tiotal+0.1) == hundratal:
#         counter_total += 1
#         ental += 1
#         hundratal += 1
#         continue
#     else:
#         ental += 1
#         hundratal += 1
#
# list_of_numbers = [0, 0, 1]
# counter_total = 0
# for i in range(0, 9):
#     list_of_numbers[0] = list_of_numbers[0] + 1
#     list_of_numbers[2] = list_of_numbers[2] + 1
#     for i in range(0, 9):
#         list_of_numbers[1] = list_of_numbers[1] + 1
#         if list_of_numbers[0] + list_of_numbers[1] is list_of_numbers[2]:
#             counter_total = + 1
#             continue
#     if list_of_numbers[0] + list_of_numbers[1] is list_of_numbers[2]:
#             counter_total =+ 1


ANSWER = counter

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.2", ANSWER, True)


dbwebb.exit_with_summary()
