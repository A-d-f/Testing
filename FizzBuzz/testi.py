import FB
import unittest

#luokka, johon listataan kaikki testattavat tapaukset
class FizzBuzzTest(unittest.TestCase):
    #testin alettava nimellä test_
    def test_Send_1_To_FB_Returns_1(self):
        #Arrange
        num = int(1)

        #Act
        result = FB.WhatToWrite(num)

        #Assert
        self.assertEqual (1, result)
    
    def test_Send_2_To_FB_Returns_2(self):
        #Arrange
        num = int(2)
        #Act
        result = FB.WhatToWrite(num)
        #Assert
        self.assertEqual (2, result)

    def test_Send_3_To_FB_Returns_FIZZ(self):
        #Arrange
        num = int(3)
        expected = "FIZZ"
        #Act
        result = FB.WhatToWrite(num)
        #Assert
        self.assertEqual (expected, result)

    def test_Send_4_To_FB_Returns_4(self):
        #Arrange
        num = int(4)
        #Act
        result = FB.WhatToWrite(num)
        #Assert
        self.assertEqual (4, result)

    def test_Send_5_To_FB_Returns_BUZZ(self):
        #Arrange
        num = int(5)
        expected = "BUZZ"
        #Act
        result = FB.WhatToWrite(num)
        #Assert
        self.assertEqual (expected, result)

    def test_Send_6_To_FB_Returns_FIZZ(self):
        #Arrange
        num = int(6)
        expected = "FIZZ"
        #Act
        result = FB.WhatToWrite(num)
        #Assert
        self.assertEqual (expected, result)

    def test_Send_7_To_FB_Returns_7(self):
        #Arrange
        num = int(7)
        #Act
        result = FB.WhatToWrite(num)
        #Assert
        self.assertEqual (7, result)

    def test_Send_9_To_FB_Returns_FIZZ(self):
        #Arrange
        num = int(9)
        expected = "FIZZ"
        #Act
        result = FB.WhatToWrite(num)
        #Assert
        self.assertEqual(expected,result)

    def test_Send_10_To_FB_Returns_BUZZ(self):
        #Arrange
        num = int(10)
        expected = "BUZZ"
        #Act
        result = FB.WhatToWrite(num)
        #Assert
        self.assertEqual (expected, result)

    def test_Send_15_To_FB_Returns_FIZZBUZZ(self):
        #Arrange
        num = int(15)
        expected = "FIZZBUZZ"
        #Act
        result = FB.WhatToWrite(num)
        #Assert
        self.assertEqual (expected, result)

    def test_Send_30_To_FB_Returns_FIZZBUZZ(self):
        #Arrange
        num = int(30)
        expected = "FIZZBUZZ"
        #Act
        result = FB.WhatToWrite(num)
        #Assert
        self.assertEqual (expected, result)

if __name__ == '__main__':
    unittest.main()