from ..titanic_utils.utils import is_adult

def test_is_adult():
    threshold = 18
    ages = [18.0, 24.0, 25.3, 42.0, 14.0, 13]
    results = [True, True, True, True, False, False]
    for age, result in zip(ages, results):
        assert is_adult(age, threshold) == result, f"The age {age} was not classified correctly!"