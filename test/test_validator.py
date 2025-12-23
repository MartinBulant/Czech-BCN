import pytest
from unittest.mock import MagicMock
import random
import string
import os
from CzechBcn.validator import Validator

BIRTHNUMBERS_FEMALE_VALID = "bins/birthnumbers_Female_valid.txt"
BIRTHNUMBERS_MALE_VALID =  "bins/birthnumbers_Male_valid.txt"


@pytest.fixture
def validator() -> MagicMock:
    return Validator()


def test_validateLength_validType(validator: Validator):
    _checkStr(validator.validateLength)

def test_validateLength_typeError_int(validator: Validator):
    _checkInt(validator.validateLength)

def test_validateLength_typeError_float(validator: Validator):
    _checkFloat(validator.validateLength)

def test_validateCharacters_validType(validator: Validator):
    _checkStr(validator.validateCharacters)

def test_validateCharacters_typeError_int(validator: Validator):
    _checkInt(validator.validateCharacters)

def test_validateCharacters_typeError_float(validator: Validator):
    _checkFloat(validator.validateCharacters)

def test_validateBirthDate_validType(validator: Validator):
    _checkStr(validator.validateBirthDate)

def test_validateBirthDate_typeError_int(validator: Validator):
    _checkInt(validator.validateBirthDate)

def test_validateBirthDate_typeError_float(validator: Validator):
    _checkFloat(validator.validateBirthDate)

def test_validateBCN_validType(validator: Validator):
    _checkStr(validator.validateBCN)

def test_validateBCN_typeError_int(validator: Validator):
    _checkInt(validator.validateBCN)

def test_validateBCN_typeError_float(validator: Validator):
    _checkFloat(validator.validateBCN)

def test_validateLength_invalidLength_1(validator: Validator):
    size = int(random.uniform(1,8))
    assert(not validator.validateLength("1"*size))

def test_validateLength_invalidLength_2(validator: Validator):
    size = int(random.uniform(11,100))
    assert(not validator.validateLength("1"*size))

def test_validateLength_validLength(validator: Validator):
    size = random.choice([9,10])
    assert(validator.validateLength("1"*size))

def test_validateCharacters_invalidLength_1(validator: Validator):
    size = int(random.uniform(1,8))
    assert(not validator.validateCharacters("1"*size))

def test_validateCharacters_invalidLength_2(validator: Validator):
    size = int(random.uniform(11,100))
    assert(not validator.validateCharacters("1"*size))

def test_validateCharacters_invalidCharacters_lowerCase_invalid(validator: Validator):
    bcnLen = random.choice([9,10])
    rg = range(bcnLen)
    bcn = [random.choice(string.digits) for _ in range(bcnLen)]
    idxs = random.sample(rg,random.randint(1,bcnLen-1))

    for idx in idxs:
        bcn[idx] = random.choice(string.ascii_lowercase)

    bcn = ''.join(bcn)
    assert(not validator.validateCharacters(bcn))

def test_validateCharacters_invalidCharacters_upperCase_invalid(validator: Validator):
    bcnLen = random.choice([9,10])
    rg = range(bcnLen)
    bcn = [random.choice(string.digits) for _ in range(bcnLen)]
    idxs = random.sample(rg,random.randint(1,bcnLen-1))

    for idx in idxs:
        bcn[idx] = random.choice(string.ascii_uppercase)

    bcn = ''.join(bcn)
    assert(not validator.validateCharacters(bcn))

def test_validateCharacters_invalidCharacters_letters_invalid(validator: Validator):
    bcnLen = random.choice([9,10])
    rg = range(bcnLen)
    bcn = [random.choice(string.digits) for _ in range(bcnLen)]
    idxs = random.sample(rg,random.randint(1,bcnLen-1))

    for idx in idxs:
        bcn[idx] = random.choice(string.ascii_letters)

    bcn = ''.join(bcn)
    assert(not validator.validateCharacters(bcn))

def test_validateCharacters_invalidCharacters_spaces_invalid(validator: Validator):
    bcnLen = random.choice([9,10])
    rg = range(bcnLen)
    bcn = [random.choice(string.digits) for _ in range(bcnLen)]
    idxs = random.sample(rg,random.randint(1,bcnLen-1))

    for idx in idxs:
        bcn[idx] = " "

    bcn = ''.join(bcn)
    assert(not validator.validateCharacters(bcn))

def test_validateBirthDate_valid(validator: Validator):
    assert(validator.validateBirthDate("6107090704"))

def test_validateBirthDate_date_invalid(validator: Validator):
    assert(not validator.validateBirthDate("6107400704"))

def test_validateBirthDate_month_invalid(validator: Validator):
    assert(not validator.validateBirthDate("6165090704"))

def test_validBCN_male_valid(validator: Validator):
    path = os.path.join(os.path.dirname(__file__),BIRTHNUMBERS_MALE_VALID)
    for bcn in _loadTestData(path):
        assert(validator.validateBCN(bcn))

def test_validBCN_female_valid(validator: Validator):
    path = os.path.join(os.path.dirname(__file__),BIRTHNUMBERS_FEMALE_VALID)
    for bcn in _loadTestData(path):
        assert(validator.validateBCN(bcn))

def test_validBCN_female_invalid(validator: Validator):
    assert(not validator.validateBCN("6452211833"))

def test_validBCN_male_invalid(validator: Validator):
    assert(not validator.validateBCN("8803022805"))

def _checkStr(function):
    assert(not function("A"))

def _checkInt(function):
    with pytest.raises(TypeError):
        function(int(12))

def _checkFloat(function):
    with pytest.raises(TypeError):
        function(float(12))

def _loadTestData(path:str) -> list:
    if not os.path.isfile(path):
        raise AttributeError(f"File in the given path does not exist. Given path '{path}'")

    with open(path, "r") as file:
        bcns = file.read().splitlines()

    return bcns