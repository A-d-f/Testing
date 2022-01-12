import kps
import unittest



class kpsTestit(unittest.TestCase):
    
    def test_onko_tasapeli(self):
        #Arrange
        val1 = 2
        val2 = 1
        

        #Act
        result = kps.Voittaja(val1, val2)
        

        #Assert
        self.assertEqual(result, "Tasapeli!")

    def test_voittaako_tietokone_playerRock(self):
        #Arrange
        val1 = 2
        val2 = 2

        #Act
        result = kps.Voittaja(val1, val2)

        #Assert
        self.assertEqual(result, "Paperi voittaa kiven. Hävisit.")

    def test_voittaako_pelaaja_playerRock(self):
        #Arrange
        val1 = 2
        val2 = 3

        #Act
        result = kps.Voittaja(val1, val2)

        #Assert
        self.assertEqual(result, "Kivi voittaa sakset. Voitit!")

    def test_voittaako_pelaaja_playerPaper(self):
        #Arrange
        val1 = 1
        val2 = 1

        #Act
        result = kps.Voittaja(val1, val2)

        #Assert
        self.assertEqual(result, "Paperi voittaa kiven. Voitit!")

    def test_voittaako_tietokone_playerPaper(self):
        #Arrange
        val1 = 3
        val2 = 3

        #Act
        result = kps.Voittaja(val1, val2)

        #Assert
        self.assertEqual(result, "Sakset voittaa paperin. Hävisit.")

    def test_voittaako_pelaaja_playerScissors(self):
        #Arrange
        val1 = 1
        val2 = 2

        #Act
        result = kps.Voittaja(val1,val2)

        #Assert
        self.assertEqual(result, "Sakset voittaa paperin. Voitit!")

    def test_voittaako_tietokone_playerScissors(self):
        val1 = 1
        val2 = 1
        #Act
        result = kps.Voittaja(val1,val2)

        #Assert
        self.assertEqual(result, "Kivi voittaa sakset. Hävisit.")

    def test_if_wrong_input(self):
        val1 = 2
        val2 = 2

        result = kps.Voittaja(val1, val2)

        self.assertEqual(result, "Väärä syöte!")




if __name__ == '__main__':
    unittest.main()

#ANNA-MARIA PALM