EXPECTED_MNINUTES_IN_OVEN = 40

def remainingMinutesInOven(TIME_ALREADY_IN_OVEN):
    return EXPECTED_MNINUTES_IN_OVEN-TIME_ALREADY_IN_OVEN

def preparationTimeInMinutes(NUMBER_OF_LAYERS):
    return NUMBER_OF_LAYERS*2

def totalTimeInMinutes(numberOfLayers, actualMinutesInOven):
    return remainingMinutesInOven(actualMinutesInOven) + preparationTimeInMinutes(numberOfLayers)

print(totalTimeInMinutes(3, 20))


