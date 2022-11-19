EXPECTED_MNINUTES_IN_OVEN = 40

def remainingMinutesInOven(TIME_ALREADY_IN_OVEN):
    TIME_ALREADY_IN_OVEN = int(TIME_ALREADY_IN_OVEN)
    return EXPECTED_MNINUTES_IN_OVEN-TIME_ALREADY_IN_OVEN

def preparationTimeInMinutes(NUMBER_OF_LAYERS):
    NUMBER_OF_LAYERS = int(NUMBER_OF_LAYERS)
    return NUMBER_OF_LAYERS*2

def totalTimeInMinutes(numberOfLayers, actualMinutesInOven):
    return int(actualMinutesInOven) + preparationTimeInMinutes(numberOfLayers)

user_layers = input("How many layers are in your lasagna? ")
user_minutesInOven = input("How many minutes has your lasagna been in the oven? ")

print("You have spent " + str(totalTimeInMinutes(user_layers, user_minutesInOven)) + " minutes on making your lasagna.")


