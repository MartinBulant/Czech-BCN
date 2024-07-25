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
        Generate a Czech birth certificate number from the given arguments.
        @param dateOfBirth [datetime.date]: date of the birth
        @param gender [Gender]: M - male, F - female
        @return [BCN]: generated birth certificate number
        """
        Generator._typeValidation(date_of_birth,date);Generator._typeValidation(gender,Gender)

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
        """
        Just check data type of the given variable.
        :param variable [any]: variable for data type check
        :param expected [any]: expected data type
        :return: None
        """
        if not isinstance(variable,expected):
            raise TypeError(f"Expected data type '{expected}', but it has been given '{type(variable)}'")
        



if __name__ == "__main__0":
    pass