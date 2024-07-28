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
        Validator._typeValidation(bcn,str)
        return  9<=len(bcn)<=10

    @staticmethod
    def validateCharacters(bcn:str) -> bool:
        """
        Validate characters of the given birth certificate number (bcn).
        :param bcn [str]: birth certificate number (BCN)
        :return [bool]: True = valid characters, False otherwise. 
        """
        Validator._typeValidation(bcn,str)
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

        Validator._typeValidation(bcn,str)
        if not Validator.validateLength(bcn):
            return False
        
        year = int(bcn[0:2])
        month = int(bcn[2:4])
        day = int(bcn[4:6])
        if not ((0 <=year<=99) and (1<=(month)<=12 or 51<=(month)<=62) and (1<=day<=31)):
            return False
        
        if month > 50:
            month -= 50

        endingLen = len(bcn[6:])
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
        Validator._typeValidation(bcn,str)
        if not Validator.validateLength(bcn): return False
        if not Validator.validateCharacters(bcn): return False
        if not Validator.validateBirthDate(bcn): return False
        if len(bcn) == 9:
            return True
        return (int(bcn)%11==0)
    
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
    
