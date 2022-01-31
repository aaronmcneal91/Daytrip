import random
# def day_trip
# refactor the 3 functions to be similar to rando_dest
# make an into print message that will explain to the user what is going on
# think about how to use a while loop to allow a user to re-select options

welcome_message = ('HELLO WELCOME TO THE TRIP RANDOMIZER!!! WOULD YOU LIKE US TO PLAN YOUR DAY?')
print(welcome_message)

def daytrip():

    welcome = input('')
      
    if(welcome == 'no'):
        print('HAVE A NICE DAY!!!')
        print(welcome_message)
        daytrip()
        


    elif(welcome == 'yes'):
        print('ONE MOMENT PLEASE!!!')
        rando_dest(dest)
        rando_rest(rest)
        rando_trans(trans)
        rando_ent(ent)


        


    



dest = ['Roanoke', 'Lynchburg', 'Blacksburg', 'Norfolk']
rest = ['Mcdonalds', 'Wendys', 'KFC', 'Popeyes']
trans = ['Foot,', 'Bike', 'Train', 'Car']
ent = ['Movies', 'Go Carts', 'Bar', 'Ski']

def rando_dest(list):
    place = random.choice(list)
    print(f'{place} has been randomly selected as your destination!')
    return place

def rando_rest(list):
    food = random.choice(list)
    print(f'{food} has been randomly selected as your resturaunt!')
    return food

def rando_trans(list):
    result = random.choice(list)
    print(f'{result} has been randomly selected as your mode of transportation!')
    return result

def rando_ent(list):
    fun = random.choice(list)
    print(f'{fun} has been randomly selected as your entertainment!')
    return fun

daytrip()

def concl(finish):
    for choice in finish:
        if finish == 'yes':
            print('have a great day!')
            daytrip()
        elif (input(finish)) == 'food' 'place''transpo' 'fun':
            print(input('please reselect'))
            res()













# def concl():
selection = (input('Are you happy with these selections?' ))

    
if selection == 'yes':
        print('Your day trip is complete, ENJOY!!!')
        daytrip()

elif selection == 'no':
        print("We're sorry! Please enter what you would like re-select randomly! Food', 'Place', 'Transpo', 'Fun")
        answer = input('')


def res():
    if answer == 'food':
        rando_rest(rest)
    elif answer == 'place':
        rando_dest(dest)
    elif answer == 'transpo':
        rando_trans(trans)
    elif answer == 'fun':
        rando_ent(ent)

res()




answ = True
True == 'yes'

print('WILL THAT BE ALL? IF NO, SELECT FOOD, PLACE, TRANSPO, OR FUN')
answ = input('')

while answ =='yes':
    print("YOU'RE TRIP IS COMPLETE!! HAVE A GREAT DAY!!!")
        
if answ =='food' 'place' 'transpo''funy':
    print('PLEASE SELECT, FOOD,PLACE TRANSPO, OR FUN')
    
concl()
        


