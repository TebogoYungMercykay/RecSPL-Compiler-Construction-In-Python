import pytest
from helpers.type_checker import check_types

print("\033[94m\n==== TYPE CHECKER: TEST CASES USING PYTEST ====\n\033[0m")

def test_pytest_is_working_1():
    assert 1 + 1 == 2, "Default Test For Type Checker Is Working!"

@pytest.mark.parametrize("file_number", range(1, 2))
def test_type_check_files_first(file_number):
    assert check_types(None, None) == False, f"{file_number}: Type Checker Default Tests Working"

@pytest.mark.parametrize("file_number", range(2, 21))
def test_type_check_files_2_to_20(file_number):
    assert check_types(None, None) == False, f"{file_number}: Type Checker - All Good"

if __name__ == "__main__":
    # pytest -v
    pytest.main(["-s -v", __file__])
