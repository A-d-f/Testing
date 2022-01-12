import random

def Pelaajanvalinta():
    pelaajan_valinta = input("Kivi, paperi vai sakset?")
    #jos pelaaja valitsee ... , muutetaan se 1
    if pelaajan_valinta in ["Kivi", "kivi", "K", "k"]:
        pelaajan_valinta = 1
    #sama paperille
    elif pelaajan_valinta in ["Paperi", "paperi", "P", "p"]:
        pelaajan_valinta = 2
    #ja saksille
    elif pelaajan_valinta in ["Sakset", "sakset", "S", "s"]:
        pelaajan_valinta = 3
    
    #Jos pelaaja valitsee jotain muuta, kuin pyydetty:
    else:
        print("Väärä syöte!")
        return "Väärä syöte!"
        
    return pelaajan_valinta

def Tietokoneenvalinta():
    #arvotaan tietokoneen valinta randomilla
    tiet_valinta = random.randint (1,3)
   
    return tiet_valinta

def Voittaja(pv,tv):
    
    if pv == 1:
        if tv == 1:
            print("Tasapeli!")
            return "Tasapeli!"
        elif tv == 2:
            print("Paperi voittaa kiven. Hävisit.")
            return "Paperi voittaa kiven. Hävisit."
        elif tv == 3:
            print("Kivi voittaa sakset. Voitit!")
            return "Kivi voittaa sakset. Voitit!"

    elif pv == 3:
        if tv == 3:
            print("Tasapeli.")
            return "Tasapeli!"
        elif tv == 2:
            print("Sakset voittaa paperin. Voitit!")
            return "Sakset voittaa paperin. Voitit!"
        elif tv == 1:
            print("Kivi voittaa sakset. Hävisit.")
            return "Kivi voittaa sakset. Hävisit."

    elif pv == 2:
        if tv == 3:
            print("Sakset voittaa paperin. Hävisit.")
            return "Sakset voittaa paperin. Hävisit."
        elif tv == 2:
            print("Tasapeli!")
            return "Tasapeli!"
        elif tv == 1:
            print("Paperi voittaa kiven. Voitit!")
            return "Paperi voittaa kiven. Voitit!"

    else:
        return "Väärä syöte!"       

if __name__ == '__main__':
    #Peli käyntiin, pelaajan syöte:
    p=Pelaajanvalinta()
    
    #Jos ei tule väärää syötettä, niin kysytään...
    if p != "Väärä syöte!":
        
        #...Tietokoneen syöte:
        t = Tietokoneenvalinta()
        Voittaja(p, t)

#Anna-Maria Palm
        