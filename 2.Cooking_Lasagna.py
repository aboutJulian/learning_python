EXPECTED_MNINUTES_IN_OVEN = 40

#This function asks the user for how long the lasagna has been in the oven already. 
#Then it converts the string into an int and substracts this int from the expected time in the oven(40 minutes).

def remainingMinutesInOven(TIME_ALREADY_IN_OVEN):
    TIME_ALREADY_IN_OVEN = int(TIME_ALREADY_IN_OVEN)
    return EXPECTED_MNINUTES_IN_OVEN-TIME_ALREADY_IN_OVEN

#This function asks the user for the amount of layers in the lasagna. 
#Then it converts the string into an int and multiplies it by 2.

def preparationTimeInMinutes(NUMBER_OF_LAYERS):
    NUMBER_OF_LAYERS = int(NUMBER_OF_LAYERS)
    return NUMBER_OF_LAYERS*2

#This function asks for the amount of layers and the time in the oven.
#Then it converts the time in the oven into an int and adds it with the result
# of giving the preperationTimeInMinutes function the number of layers.

def totalTimeInMinutes(numberOfLayers, actualMinutesInOven):
    return int(actualMinutesInOven) + preparationTimeInMinutes(numberOfLayers)

#This is just a simple user input to show that the programm is working.

user_layers = input("How many layers are in your lasagna? ")
user_minutesInOven = input("How many minutes has your lasagna been in the oven? ")

print("You have spent " + str(totalTimeInMinutes(user_layers, user_minutesInOven)) + " minutes on making your lasagna.")


