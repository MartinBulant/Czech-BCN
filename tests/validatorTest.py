import unittest
import random
import string
from src.validator import Validator


class TestValidator(unittest.TestCase):
    def test_validateLength_invalidLength_1(self) -> None:
        size = int(random.uniform(1,8))
        self.assertFalse(Validator.validateLength("1"*size))
        
    def test_validateLength_invalidLength_2(self) -> None:
        size = int(random.uniform(11,100))
        self.assertFalse(Validator.validateLength("1"*size))

    def test_validateLength_validLength(self) -> None:
        size = random.choice([9,10])
        self.assertTrue(Validator.validateLength("1"*size))

    def test_validateCharacters_invalidLength_1(self) -> None:
        size = int(random.uniform(1,8))
        self.assertFalse(Validator.validateCharacters("1"*size))
    
    def test_validateCharacters_invalidLength_2(self) -> None:
        size = int(random.uniform(11,100))
        self.assertFalse(Validator.validateCharacters("1"*size))
    
    def test_validateCharacters_invalidCharacters_lowerCase_invalid(self) -> None:
        bcnLen = random.choice([9,10])
        rg = range(bcnLen)
        bcn = [random.choice(string.digits) for _ in range(bcnLen)]
        idxs = random.sample(rg,random.randint(1,bcnLen-1))
        
        for idx in idxs:
            bcn[idx] = random.choice(string.ascii_lowercase)

        bcn = ''.join(bcn)
        self.assertFalse(Validator.validateCharacters(bcn))

    def test_validateCharacters_invalidCharacters_upperCase_invalid(self) -> None:
        bcnLen = random.choice([9,10])
        rg = range(bcnLen)
        bcn = [random.choice(string.digits) for _ in range(bcnLen)]
        idxs = random.sample(rg,random.randint(1,bcnLen-1))
        
        for idx in idxs:
            bcn[idx] = random.choice(string.ascii_uppercase)

        bcn = ''.join(bcn)
        self.assertFalse(Validator.validateCharacters(bcn))
    
    def test_validateCharacters_invalidCharacters_letters_invalid(self) -> None:
        bcnLen = random.choice([9,10])
        rg = range(bcnLen)
        bcn = [random.choice(string.digits) for _ in range(bcnLen)]
        idxs = random.sample(rg,random.randint(1,bcnLen-1))

        for idx in idxs:
            bcn[idx] = random.choice(string.ascii_letters)
        
        bcn = ''.join(bcn)
        self.assertFalse(Validator.validateCharacters(bcn))

    def test_validateCharacters_invalidCharacters_spaces_invalid(self) -> None:
        bcnLen = random.choice([9,10])
        rg = range(bcnLen)
        bcn = [random.choice(string.digits) for _ in range(bcnLen)]
        idxs = random.sample(rg,random.randint(1,bcnLen-1))

        for idx in idxs:
            bcn[idx] = " "

        bcn = ''.join(bcn)
        self.assertFalse(Validator.validateCharacters(bcn))
    
    def test_validateBirthDate_date_invalid(self) -> None:
        bcn = 

    def test_validateBirthDate_month_invalid(self) -> None:
        pass

    def test_validateBirthDate_year_invalid(self) -> None:
        pass

    

    


if __name__ =="__main__":
    unittest.main()