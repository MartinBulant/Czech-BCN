from dataclasses import dataclass
from datetime import date
import random
import calendar

@dataclass
class Gender:
    Male:str = "M"
    Female:str = "F"

@dataclass
class BCN:
    code:str
    birthDay:date
    gender:str

    def __str__(self) -> str:
        ret = f"code: {self.code}\nbirthDay: {self.birthDay}\ngender: {self.gender}"
        return ret 

BIRTHCODETHRESHOLD = 1954

class Generator:
    @staticmethod
    def randomBcn(min:int=0,max:int=99) -> BCN:
        """
        Create random a random czech birth certificate number (BCN) in the range from mim to max.
        :param min [int]: min value of the range
        :param max [int]: max value of the range
        :return [BCN]: generated BCN
        """
        Generator._typeValidation(min,int);Generator._typeValidation(max,int)
        delta = round(random.uniform(min,max))
        randomDate = Generator._generateRandomDate(delta)
        return Generator.generateBCN(randomDate,Generator._getRandomGender())
    
    @staticmethod
    def randomGender(birthDate:date) -> BCN:
        """
        Generate random BCN from given birth date.
        :param birthDate [date]: date of the birth
        :return [BCN]: generated birth certificate number (BCN)
        """
        return Generator.generateBCN(birthDate,Generator._getRandomGender())

    @staticmethod
    def randomBirthDate(gender:str,min:int=0,max:int=99) -> BCN:
        """
        Generate random BCN from given birth gender.
        :param birthDate [date]: date of the birth
        :param min [int]: min value of the generator range
        :param max [int]: max value of the generator range
        :return [BCN]: generated birth certificate number (BCN)
        """
        delta = round(random.uniform(min,max))
        randomDate = Generator._generateRandomDate(delta)
        return Generator.generateBCN(randomDate,gender)
    
    @staticmethod
    def generateBCN(birthDate:date, gender:str) -> BCN:
        """
        Generate a Czech birth certificate number from the given arguments.
        :param birthDate [datetime.date]: date of the birth
        :param gender [Gender]: M - male, F - female
        :return [BCN]: generated birth certificate number
        """
        Generator._typeValidation(birthDate,date);Generator._typeValidation(gender,str)
        if (gender != Gender.Male) and (gender != Gender.Female):
            raise ValueError(f"It was given '{gender}', but it should be M or F.")

        birth_code = ""
        year = str(birthDate.year)[-2:]
        month = str(birthDate.month).zfill(2)

        if gender == Gender.Female:
            month = str(int(month) + 50)
        day = str(birthDate.day).zfill(2)

        birth_code += year
        birth_code += month
        birth_code += day
        control_code = "".join(str(random.randint(0, 9)) for _ in range(0, 3)) 

        birth_code = str(birth_code) + control_code

        if int(birthDate.year) < BIRTHCODETHRESHOLD:
            return BCN(birth_code,birthDate,gender)
        return BCN(birth_code + str((int(birth_code) % 11)),birthDate,gender)

    @staticmethod
    def _generateRandomDate(delta:int) -> date:
        """
        Generate random date.
        :param delta [int]: delta from current year
        :return [date]: generated random date
        """
        Generator._typeValidation(delta,int)
        year = round(date.today().year - delta)
        month = round(random.uniform(1,12))
        days = calendar.monthrange(year,month)[1]
        day = round(random.uniform(1,days))
        return date(year,month,day)
    
    @staticmethod
    def _getRandomGender() -> str:
        """
        Randomly choose gender.
        :param: None
        :return [str]: random gender
        """
        return random.choice([Gender.Male,Gender.Female])

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
        

if __name__ == "__main__":
    pass