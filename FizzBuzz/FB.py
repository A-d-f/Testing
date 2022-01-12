def WhatToWrite(value):

    #tarkistetaan, onko arvo jaollinen kolmella ja viidellä, palauttaa fizzbuzz. Rajaavin ehto ekaksi
    if (value % 3 == 0 and value % 5 == 0):
        return "FIZZBUZZ"

    #tarkistetaan, onko numero jaollinen kolmella
    if value % 3 == 0:
        return "FIZZ"

    #tarkistetaan, onko numero jaollinen viidellä
    if value % 5 == 0:
        return "BUZZ"

    return value