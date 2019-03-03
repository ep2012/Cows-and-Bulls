#Project created by: Eli Price
#Created as a sample project to get to know Python
#! /usr/bin/pythonw python
import random

INVALID_NUMBER = "invalid number"

def format_number(number = INVALID_NUMBER) :
    try :
        int(number) #cast the number to make sure it was properly passed in by the user
        number = str(number)
        if len(number) == 4 : return number
        elif len(number) == 3 : return "0" + number
        elif len(number) == 2 : return "00" + number
        elif len(number) == 1 : return "000" + number
        else : return INVALID_NUMBER
    except :
        return INVALID_NUMBER

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
print("You may exit at any time by entering 'exit'")
print("but this makes everything escape")

while user_results['target_number'] != user_results['guess'] :
    user_results['guess'] = raw_input("Enter your guess: ")
    if user_results['guess'].lower() == "exit" : break
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

if all(user_results['number_by_number_results']) :
    print("Number of total escaped cows: " + str(user_results['num_cows']))
    print("Number of total escaped bulls: " + str(user_results['num_bulls']))
    if(user_results['num_cows'] + user_results['num_bulls'] == 4) : print("Perfect!")
    elif(user_results['num_cows'] + user_results['num_bulls'] <= 20) : print("Oh dang! You got it!")
    elif(user_results['num_cows'] + user_results['num_bulls'] <= 30) : print("Finally under control! Now you just gotta look for a missing herd.")
    else : print("At least it's closed. Now time to send out the swad to recover all that cattle!")
else :
    print("You lost, all of the cows and bulls escaped!")
