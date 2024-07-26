import re

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
        return re.search("\D",bcn) is None

    @staticmethod
    def validateBirthDate(bcn:str) -> bool:
        """
        Validate birth date in the given birth certificate number (BCN).
        :param bcn [str]: birth certificate number
        :return [bool]: True = valid, False otherwise.
        """
        if not Validator.validateLength(bcn):
            return False
        day = int(bcn[0:2])
        month = int(bcn[2:4])
        year = int(bcn[4:6])
        return  (0 <=year<=99) and( 1<=(month)<=12 or 51<=(month)<=62) and(1<=day<=31)

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
