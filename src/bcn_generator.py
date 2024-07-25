from dataclasses import dataclass
from datetime import date
import random

@dataclass
class Gender:
    Male:str = "M"
    Female:str = "F"

@dataclass
class BCN:
    code:str
    birthDay:date
    gender:Gender

BIRTHCODETHRESHOLD = 1954

class Generator:
    
    @staticmethod
    def randomBcn(min:int=0,max:int=99) -> BCN:
        raise NotImplementedError
    
    @staticmethod
    def randomGender(birthDate:date) -> BCN:
        raise NotImplementedError

    @staticmethod
    def randomBirthDate(gender:Gender) -> BCN:
        raise NotImplementedError
    
    @staticmethod
    def generateBCN(date_of_birth:date, gender:Gender) -> BCN:
        """
        Generate random birth code.
        @param dateOfBirth [datetime.date]: date of the birth
        @param gender [str]: M - male, F - female
        @return [str]: generated birth code
        """
        raise NotImplementedError
        birth_code = ""
        year = str(date_of_birth.year)[-2:]
        month = str(date_of_birth.month).zfill(2)

        if gender.upper() == Gender.Female:
            month = str(int(month) + 50)
        day = str(date_of_birth.day).zfill(2)

        birth_code += year
        birth_code += month
        birth_code += day
        control_code = "".join(str(random.randint(0, 9)) for _ in range(0, 3)) 

        birth_code = str(birth_code) + control_code

        if int(date_of_birth.year) < BIRTHCODETHRESHOLD:
            return birth_code
        return birth_code + str((int(birth_code) % 11))

    @staticmethod
    def _typeValidation(variable,expected) -> None:
        raise NotImplementedError
        



if __name__ == "__main__0":
    pass