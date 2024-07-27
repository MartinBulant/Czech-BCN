import unittest
import random
import string
import os
from src.validator import Validator

BIRTHNUMBERS_FEMALE_VALID = "./bins/birthnumbers_Female_valid.txt" 
BIRTHNUMBERS_MALE_VALID =  "./bins/birthnumbers_Male_valid.txt"




class TestValidator(unittest.TestCase):

    def test_validateLength_validType(self) -> None:
        self._checkStr(Validator.validateLength)

    def test_validateLength_typeError_int(self) -> None:
        self._checkInt(Validator.validateLength)
        
    def test_validateLength_typeError_float(self) -> None:
        self._checkFloat(Validator.validateLength)

    def test_validateCharacters_validType(self) -> None:
        self._checkStr(Validator.validateCharacters)

    def test_validateCharacters_typeError_int(self) -> None:
        self._checkInt(Validator.validateCharacters)
        
    def test_validateCharacters_typeError_float(self) -> None:
        self._checkFloat(Validator.validateCharacters)

    def test_validateBirthDate_validType(self) -> None:
        self._checkStr(Validator.validateBirthDate)

    def test_validateBirthDate_typeError_int(self) -> None:
        self._checkInt(Validator.validateBirthDate)
        
    def test_validateBirthDate_typeError_float(self) -> None:
        self._checkFloat(Validator.validateBirthDate)
        
    def test_validateBCN_validType(self) -> None:
        self._checkStr(Validator.validateBCN)

    def test_validateBCN_typeError_int(self) -> None:
        self._checkInt(Validator.validateBCN)
        
    def test_validateBCN_typeError_float(self) -> None:
        self._checkFloat(Validator.validateBCN)
        
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
    
    def test_validateBirthDate_valid(self) -> None:
        self.assertFalse(Validator.validateBirthDate("6107090704"))
    
    def test_validateBirthDate_date_invalid(self) -> None:
        self.assertFalse(Validator.validateBirthDate("6107500704"))

    def test_validateBirthDate_month_invalid(self) -> None:
        self.assertFalse(Validator.validateBirthDate("6157090704"))

    def test_validBCN(self)

    def _checkStr(self,function) -> None:
        self.assertFalse(function("A"))

    def _checkInt(self,function) -> None:
        with self.assertRaises(TypeError):
            function(int(12))
    
    def _checkFloat(self,function) -> None:
        with self.assertRaises(TypeError):
            function(float(12))
    
    def _loadTestData(self,path:str) -> list:
        if not os.path.isfile(path):
            raise AttributeError("File in the given path does not exist.")
        
        with open("tests/bins/birthnumbers_Male.txt", "r") as file:
            bcns = file.read().splitlines()

        return bcns

if __name__ =="__main__":
    unittest.main()