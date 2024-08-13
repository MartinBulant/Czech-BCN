import unittest
from src.generator import Generator
from src.validator import Validator

class TestGenerator(unittest.TestCase):
    
    def test_randomBcn_invalid_data_type_min_parameter(self) -> None:
        with self.assertRaises(TypeError):
            Generator.randomBcn(min="a")
    
    def test_randomBcn_invalid_data_type_max_parameter(self) -> None:
        with self.assertRaises(TypeError):
            Generator.randomBcn(max="a")

    def test_randomBcn_valid(self) -> None:
        for i in range(1000):
            with self.subTest(f"check of the {i}-th bcn"):
                bcn = Generator.randomBcn()
                self.assertTrue(Validator.validateBCN(bcn.code),msg=f"\ninvalid bcn:\n{bcn}")

    def test_randomGender_valid(self) -> None:
        raise NotImplementedError
    
    def test_randomBirthDate_valid(self) -> None:
        raise NotImplementedError
    
    def test_generateBCN_valid(self) -> None:
        raise NotImplementedError



if __name__ =="__main__":
    unittest.main()