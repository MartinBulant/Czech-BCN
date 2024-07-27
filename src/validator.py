import re
import datetime

class Validator:

    @staticmethod
    def validateLength(bcn:str) -> bool:
        """
        Validate length of the birth certificate number (BCN).
        :param bcn [str]: birth certificate number (BCN)
        :return [bool]: True = valid length, False otherwise.
        """
        return  9<=len(bcn)<=10

    @staticmethod
    def validateCharacters(bcn:str) -> bool:
        """
        Validate characters of the given birth certificate number (bcn).
        :param bcn [str]: birth certificate number (BCN)
        :return [bool]: True = valid characters, False otherwise. 
        """
        if not Validator.validateLength(bcn): return False
        return re.search("\D",bcn) is None

    @staticmethod
    def validateBirthDate(bcn:str) -> bool:
        """
        Validate birth date in the given birth certificate number (BCN).
        :param bcn [str]: birth certificate number
        :return [bool]: True = valid, False otherwise.
        """
        def yearDecoding(year:int,endingLen:int) -> int:
            if (endingLen==3) and (year > 53):
                return year + 1800
            elif ((endingLen==3) and (year <= 53)) or ((endingLen==4) and (year > 53)):
                return year + 1900
            elif (endingLen==4) and (year <= 53):
                return year + 2000
            else:
                raise AttributeError

        if not Validator.validateLength(bcn):
            return False
        day = int(bcn[0:2])
        month = int(bcn[2:4])
        year = int(bcn[4:6])
        if not ((0 <=year<=99) and (1<=(month)<=12 or 51<=(month)<=62) and (1<=day<=31)):
            return False
        
        if month > 50:
            month -= 50

        endingLen = int(bcn[6:-1])
        year = yearDecoding(year,endingLen) 
        try:
            datetime.date(year,month,day)
        except ValueError:
            return False
        else:
            return True

    @staticmethod
    def validateBCN(bcn:str) -> bool:
        """
        Validate the given birth certificate number.
        :param bcn [str]: birth certificate number
        :return: True - valid, False otherwise.
        """
        if not Validator.validateLength(bcn): return False
        if not Validator.validateCharacters(bcn): return False
        if not Validator.validateBirthDate(bcn): return False
        if len(bcn) == 9:
            return True
        return int(bcn[0:-1])%11==0
        

if __name__ == "__main__":
    pass
    
