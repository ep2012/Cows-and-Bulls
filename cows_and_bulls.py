#Project created by: Eli Price
#Created as a sample project to get to know Python
#! /usr/bin/pythonw python
import random

INVALID_NUMBER = "invalid number"

def format_number(number = 0000) :
    number = str(number)
    if len(number) == 4 : return str(number)
    elif len(number) == 3 : return "0" + str(number)
    elif len(number) == 2 : return "00" + str(number)
    elif len(number) == 1 : return "000" + str(number)
    else : return INVALID_NUMBER

user_results = {
    'number_by_number_results' : [bool(0),bool(0),bool(0),bool(0)],
    'num_cows' : 0,
    'num_bulls' : 0,
    'guess' : "",
    'target_number' : format_number(random.randint(0,9999))
}

print("Welcome to the Cows and Bulls Game!")
print("Enter a 4 digit number - ")
print("it will be compared to a random 4 digit number")
print("Each digit that is correct, a cow escapes.")
print("Each time you previously guessed a digit and")
print("the digit is now incorrect, a bull escapes.")
print("Once you guess all 4 digits, the game ends and they stop escaping.")
print("The goal is to have the least amount of cows and bulls escape.")

while user_results['target_number'] != user_results['guess'] :
    user_results['guess'] = input("Enter your guess or exit() to exit: ")
    user_results['guess'] = format_number(user_results['guess'])

    if user_results['guess'] == INVALID_NUMBER : print(INVALID_NUMBER)
    else :
        num_new_cows = 0
        num_new_bulls = 0
		
        for i in range(0, 4):
            if user_results['guess'][i] == user_results['target_number'][i] :
                user_results['number_by_number_results'][i] = bool(1)
                num_new_cows = num_new_cows + 1
            else :
                if user_results['number_by_number_results'][i] == bool(1) : num_new_bulls = num_new_bulls + 1
                user_results['number_by_number_results'][i] = bool(0)
        print("Number of newly escaped cows: " + str(num_new_cows))
        print("Number of newly escaped bulls: " + str(num_new_bulls))
        user_results['num_cows'] = user_results['num_cows'] + num_new_cows
        user_results['num_bulls'] = user_results['num_bulls'] + num_new_bulls

print("Number of total escaped cows: " + str(user_results['num_cows']))
print("Number of total escaped bulls: " + str(user_results['num_bulls']))
if all(user_results['number_by_number_results']) : print ("You win!")
